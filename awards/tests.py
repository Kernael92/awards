from django.test import TestCase
from .models import Profile,Project
from django.contrib.auth.models import User

# Create your tests here.

# class ProfileTestClass(TestCase):
#     # set up method
#     def setUp(self):
#         # #Creating a new user 
#         # self.glenn = User(username="Glenn",email="example@gmail.com",password="cbhwhe")
#         # self.save_user()
#         #creating a new profile and saving it
#         self.new_profile = Profile(user = self.glenn,profile_pic="image.jpg",bio="Geospatial engineer, fashion lover", email="example@gmail.com", phone_number="0714140423")
#         self.new_profile.save()
#     # Testing instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.glenn,Profile))
    
class ProjectTestClass(TestCase):
    # set up method
    def setUp(self):
        # creating a new profile
        self.new_profile = Profile(user = self.glenn,profile_pic="image.jpg",bio="Geospatial engineer, fashion lover", email="example@gmail.com", phone_number="0714140423")
        self.new_profile.save()
        #creating a new project
        self.new_project = Project(user_profile = self.profile, title = "Instagram",project_image = "image.jpg",project_description = "A web page to allow users to post their photos and comment on other users photos",project_link = "https://kernel-instgaram.herokuapp.com/")
        self.new_project.save()
