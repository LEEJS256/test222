from django.db import models
class Curriculum(models.Model):
    id= models.IntegerField(primary_key=True)
    sido = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    medical= models.IntegerField(blank=True,null=False) 
    room= models.IntegerField(blank=True,null=False)
    tel = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
