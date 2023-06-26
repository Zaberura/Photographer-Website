from django.db import models

# Create your models here.
from storages.backends.s3boto3 import S3Boto3Storage


def get_photo_upload_path(instance, filename):
    # Get the project name from the instance
    project_name = instance.name

    if project_name is None:
        project_name = "gallery"

    # Construct the upload path with the project name
    upload_path = f'photos/{project_name}/{filename}'
    return upload_path


class Project(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    season = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(storage=S3Boto3Storage(), upload_to=get_photo_upload_path, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Get the current photo field value
        current_photo = self.photo

        # Save the model to generate an ID for the project
        super().save(*args, **kwargs)

        new_path = f'photos/{self.name}/{self.photo.name}'

        if current_photo and current_photo != self.photo:
            self.photo.storage.delete(self.photo.name)
            self.photo.name = new_path
            self.photo.storage.save(new_path, self.photo)


class Tag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)


class Recipient(models.Model):
    email = models.CharField(max_length=255, null=False)


class DynamicParam(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class PhotoSource(models.Model):
    photo = models.ImageField(storage=S3Boto3Storage(), upload_to=get_photo_upload_path, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True, blank=True)  # created at  - in database
    gallery_order = models.IntegerField(null=True)
    name = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        current_photo = self.photo

        super().save(*args, **kwargs)

        new_path = f'photos/{self.name}/{self.photo.name}'

        if current_photo and current_photo != self.photo:
            self.photo.storage.delete(self.photo.name)
            self.photo.name = new_path
            self.photo.storage.save(new_path, self.photo)


def get_photo_by_project_name(project):
    from django.db import connection, transaction

    cursor = connection.cursor()

    cursor.execute(
        "SELECT ps.photo FROM website_project wp JOIN website_photosource ps ON wp.id = ps.name_id WHERE REPLACE(wp.name,' ','') = %s ",
        [project])

    row = cursor.fetchone()
    return row
