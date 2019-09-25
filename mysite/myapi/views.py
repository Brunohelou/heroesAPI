# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import HeroSerializer, UserProfileSerializer
from .models import Hero, UserProfile




class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
    
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('user')
    serializer_class = UserProfileSerializer
    