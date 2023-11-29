from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    image = models.ImageField(upload_to="image")
    full_name = models.CharField(max_length=50, blank=True , null=True)
    bio = models.CharField(max_length=200, blank=True , null=True)
    phone = models.CharField(max_length=200, blank=True , null=True)
    
    def __str__(self):
        return self.full_name
    
class ContantUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.full_name
    