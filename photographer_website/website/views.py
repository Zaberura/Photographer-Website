import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import models
from django.conf import settings
from django.core.mail import send_mail


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


def contacts(request: HttpRequest):
    if request.method == "POST":
        data = json.loads(request.body)

        subject = "Message from my own site"
        message = f"PHONE : {data['phone']}\nNAME : {data['name']}\nEMAIL : {data['email']}\n\n MESSAGE:\n\t{data['message']}"

        recipient = [recipient.email for recipient in models.Recipient.objects.all()]
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient)
        return HttpResponse("OK")
    return render(request, "contact.html")
