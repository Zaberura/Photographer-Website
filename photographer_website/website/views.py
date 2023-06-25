from django.shortcuts import render

from . import models
from django.conf import settings


# Create your views here.


def home(request):
    photos = models.PhotoSource.objects.filter(is_available=True).order_by("gallery_order")

    return render(request, 'gallery.html', {"list": photos})


def projects(request):
    all_projects = models.Project.objects.all()

    return render(request, "projects.html", {"list": all_projects})


def photo_projects(request, project: str):
    project = project.upper()

    all_photos = models.get_photo_by_project_name(project)
    photos = []

    if all_photos is not None:
        photos = [settings.MEDIA_URL + photo for photo in all_photos]

    return render(request, "gallery.html", {"list": photos})
