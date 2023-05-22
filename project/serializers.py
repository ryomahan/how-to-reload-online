from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Project


class ListUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ListProject(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
