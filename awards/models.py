from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 60)
    project_image = models.ImageField(upload_to = 'projects/')
    project_description = models.TextField()
    project_link = models.URLField(max_length = 245,)
    pub_date = models.DateTimeField(auto_now_add=True)

    def create_user_profile(sender, instance, created, **kwargs):
        if created: 
            Profile.objects.create(user=instance)
    post_save.connect(create_user_profile, sender=User)


    
    def save_project(self):
        self.save()
    def delete_project(self):
        self.delete()
    def __str__(self):
        return self.title
    
    @classmethod
    def search_projects(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'profile_pics/')
    bio = models.CharField(max_length = 254)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True)
    project = models.ForeignKey(Project,null=True)


    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
    

    def __str__(self):
        return self.user.username
    
    






