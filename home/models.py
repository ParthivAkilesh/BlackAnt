from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class StudentInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    degree = models.CharField(max_length=200, null=True)
    branch = models.CharField(max_length=200, null=True)
    degreePercentage = models.CharField(max_length=200,null=True)
    yop = models.CharField(max_length=200,null=True)
    linkedin = models.CharField(max_length=200, null=True)
    mobno = models.CharField(max_length=200, null=True)
    resume = models.FileField(upload_to='resume/', null=True)
    profile = models.ImageField(upload_to='profile/', null=True)
    placementStatus = models.BooleanField(default=False)
