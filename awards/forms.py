from .models import Project,Profile,Review
from django import forms
from django.forms import ModelForm,Textarea, IntegerField

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'project_image','project_description','project_link']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio','email']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'usability_rating', 'design_rating', 'content_rating' , 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }