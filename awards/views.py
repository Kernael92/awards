from django.shortcuts import render,redirect
from .models import Project,Profile
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, "awards/index.html",{"projects":projects})