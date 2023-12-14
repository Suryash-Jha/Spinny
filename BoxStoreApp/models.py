from django.db import models

# Create your models here.
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

