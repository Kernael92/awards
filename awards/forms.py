from .models import Project,Profile
from django import forms
from django.forms import ModelForm

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'project_image','project_description','project_link']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio','email']