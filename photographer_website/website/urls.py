from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects", views.projects, name="projects"),
    path("projects/<str:project>", views.photo_projects, name="photo_project"),
    path("contact", views.contacts, name="contact")
]
