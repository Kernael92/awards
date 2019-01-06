from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime
import numpy as np
from django.db.models import Avg, Max, Min


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

    def average_content(self):
        content_ratings = list(map(lambda x: x.content_rating, self.reviews.all()))
        return np.mean(content_ratings)













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

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    project = models.ForeignKey(Project, null=True,blank=True, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='reviews')
    comment = models.TextField()
    content_rating = models.IntegerField(choices=RATING_CHOICES,default=0)
    design_rating = models.IntegerField(choices=RATING_CHOICES,default=0)
    usability_rating = models.IntegerField(choices=RATING_CHOICES,default=0)

    def save_comment(self):
        self.save()
    def get_comment(self, id):
        comments = Review.objects.filter(project_id = id)
        return comments
    def __str__(self):
        return self.comment




    






