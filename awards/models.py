from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'profile_pics/')
    bio = models.CharField(max_length = 254)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    user_profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length = 60)
    project_image = models.ImageField(upload_to = 'projects/')
    project_description = models.TextField()
    project_link = models.URLField(max_length = 245,)

    def __str__(self):
        return self.title





