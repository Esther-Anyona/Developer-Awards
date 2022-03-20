from django.test import TestCase
from .models import *
# Create your tests here.
"""
Test methods for Profile
"""
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user='user1', profile_pic='testpic', bio='I love my veggies', contact=0)
        self.profile.save_profile()
def test_save(self):
    self.profile.save_profile()
    profiles=Profile.objects.all()
    self.assertTrue(len(profiles)>0)

def test_delete(self):
    self.profile.delete_profile()
    profiles=Profile.objects.all()
    self.assertTrue(len(profiles)==0)
    