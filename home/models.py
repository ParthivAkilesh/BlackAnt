from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class StudentInfo(models.Model):


    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Other fields for your model

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.id = uuid.uuid4()
    #     return super().save(*args, **kwargs)
    
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    degree = models.CharField(max_length=200, null=True)
    branch = models.CharField(max_length=200, null=True)
    degreePercentage = models.CharField(max_length=200,null=True)
    yop = models.CharField(max_length=200,null=True)
    linkedin = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=200, null=True)
    placementStatus = models.BooleanField(default=False)


