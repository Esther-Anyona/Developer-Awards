from rest_framework import serializers
from .models import Profile, Project
from dataclasses import fields


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'profile_pic', 'bio', 'contact')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('author', 'project_image', 'title', 'description', 'profile', 'project_url', 'date_created', 'location', 'tags', 'like')
