
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=224,null=True,blank=True)
    last_name = models.CharField(max_length=224,null=True,blank=True)
    company_name = models.CharField(max_length=224,null=True,blank=True)
    city = models.CharField(max_length=224,null=True,blank=True)
    state = models.CharField(max_length=224,null=True,blank=True)
    zip = models.IntegerField(null=True,blank=True)
    email = models.CharField(max_length=224,null=True,blank=True)
    web = models.CharField(max_length=224,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)