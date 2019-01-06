from django.shortcuts import render,redirect
from .models import Project,Profile
from django.contrib.auth.models import User
from .forms import NewProjectForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, "awards/index.html",{"projects":projects})
@login_required
def new_project(request):
    current_user = request.user 
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.user = current_user
            project.save()
        return redirect ('index')
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {'form': form})
@login_required
def profile_setting(request,username):
    user = User.objects.get(username=username)
    if request.user != user:
        return redirect('index')
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = user
            profile.save
        return redirect (reverse('profile',{'username':user.username}))
    else:
        form = ProfileForm()
    context = {
        'user': user,
        'form': form
    }
    return redirect(request, 'awards/profile_setting.html', context)
def profile(request,username):
    user = User.objects.get(username=username)
    if not user:
        return redirect('index')
    profile = Profile.objects.get(user=user)
    context = {
        'username':username,
        'user': user,
        'profile': profile,
    }

    return render(request, 'awards/profile.html', context)
def search_projects(request):
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'awards/search.html', {"message": message, "projets": searched_projects})
    else:
        message = "You haven't searched for any term"
        return render(request, 'awards/search.html', {"message": message} )









