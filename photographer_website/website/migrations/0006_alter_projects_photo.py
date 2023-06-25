# Generated by Django 4.2.2 on 2023-06-25 20:30

from django.db import migrations, models
import storages.backends.s3boto3
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_projects_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to=website.models.get_photo_upload_path),
        ),
    ]