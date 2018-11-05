from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home_view(request, *args, **kwargs):
    return  render(request, "home.html", {})

def resume_view(request, *args, **kwargs):
    return  render(request, "resume.html", {})

def guestbook(request, *args, **kwargs):
    return  render(request, "guestbook.html", {})

def project_view(request, *args, **kwargs):
    return  render(request, "project.html", {})
