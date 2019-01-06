from django.shortcuts import render,redirect,get_object_or_404
from .models import Project,Profile,Review
from django.contrib.auth.models import User
from .forms import NewProjectForm,ProfileForm,ReviewForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http  import HttpResponse, Http404, HttpResponseRedirect, JsonResponse

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, "awards/index.html",{"projects":projects})
@login_required
def new_project(request):
    current_user = request.user 
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES,)
        if form.is_valid():
            project = form.save(commit = False)
            project.user = current_user
            project.save()
        return redirect ('index')
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {'form': form})
@login_required
def profile_setting(request,):
    current_user = request.user 
   
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=current_user.profile)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = current_user
            profile.save
        return redirect('index')
        
    else:
        form = ProfileForm()
    context = {
        'form': form
    }
    return render(request, 'awards/profile_setting.html', context)
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

@login_required       
def project(request, id):
    
    project = Project.objects.get(pk = id)
    current_user = request.user
    comments = Review.get_comment(Review,id)
    review_list = Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data['design_rating']
            usability_rating = form.cleaned_data['usability_rating']
            content_rating = form.cleaned_data['content_rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review.project = project
            review.user = current_user
            review.comment = comment
            review.design_rating = design_rating
            review.usability_rating = usability_rating
            review.content_rating = content_rating
            review.save()
    else:
        form = ReviewForm

        
    context = {
        'id': id,
        'project': project,
        'form':form,
        'comments':comments,
        'review_list':review_list

    }
    return render(request, 'awards/project.html', context)









