from django.db import models
from django.contrib.auth.models import AbstractUser

class BoxModel(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    area= models.IntegerField()
    volume= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)
    
    class Meta:
        db_table = "BoxModel"

class customUser(AbstractUser):
    id= models.AutoField(primary_key=True)
    usernamex = models.CharField(max_length=100)
    passwordx = models.CharField(max_length=100)
    typex = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "customUser"

class constraints(models.Model):
    id= models.AutoField(primary_key=True)
    A1 = models.IntegerField(default=100)
    V1 = models.IntegerField(default=1000)
    L1 = models.IntegerField(default=100)
    L2 = models.IntegerField(default=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "constraints"

