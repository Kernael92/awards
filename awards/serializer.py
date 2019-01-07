from rest_framework import serializers
from .models import Profile, Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','profile_pic','bio','email','project')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','project_image','project_description','project_link','pub_date')
