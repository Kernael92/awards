from django.shortcuts import render,redirect
from .models import Project,Profile
from django.contrib.auth.models import User
from .forms import NewProjectForm
from django.contrib.auth.decorators import login_required.

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, "awards/index.html",{"projects":projects})
@login_required
def new_project(request):
    current_user = request.User 
    if request.metod == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.user_profile = current_user
            project.save()
        return redirect ('/')
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {'form': form})

