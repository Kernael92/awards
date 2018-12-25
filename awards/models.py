from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 30)
    project_image = models.ImageField(upload_to = 'projects/')
    project_description = models.TextField()
    project_link = models.URLField(max_length = 245, blank = True)


