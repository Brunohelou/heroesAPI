from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Hero(models.Model):

    PUBLISHER_CHOICES = (
        ("DC", "DC" ),
        ('MARVEL', "Marvel"),
        ("OTHER", "Other"),
    )


    id          =       models.IntegerField(primary_key=True)
    name        =       models.CharField(max_length=60)
    alias       =       models.CharField(max_length=60)
    image       =       models.ImageField(upload_to='images/', null=True, editable= True)
    description =       models.TextField(null= True, editable = True)
    publisher   =       models.CharField(max_length=30, choices=PUBLISHER_CHOICES,null=True, editable= True )
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="person", primary_key=True)
    description= models.CharField(max_length= 100, default='')
    heroes = models.ManyToManyField(Hero, related_name='herolist')
     

