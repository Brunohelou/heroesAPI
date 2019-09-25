# serializers.py
from rest_framework import serializers

from .models import Hero, UserProfile

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'alias', 'image', 'description', 'publisher')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'description','heroes')
