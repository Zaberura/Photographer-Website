from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.


def home(request):
    return render(request, 'gallery.html')


def projects(request):
    all_projects = models.Projects.objects.all()

    return render(request, "projects.html", {"list": all_projects})
