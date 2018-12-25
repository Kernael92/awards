from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 30)
    project_image = models.ImageField(upload_to = 'projects/')
    project_description = models.TextField()
    project_link = models.URLField(max_length = 245,)

    def __str__(self):
        return self.title
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profiles/')
    bio = models.CharField(max_length = 254)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True)





