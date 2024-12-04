from django.db import models

# Create your models here.
class ClassList(models.Model):
    first_name=models.CharField(null=True,blank=True,max_length=50)
    last_name=models.CharField(null=True,blank=True,max_length=50)
