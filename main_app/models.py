from django.db import models

# Create your models here.
class Class_Kaligrafi(models.Model):
    kd = models.CharField(max_length=150)
    nama = models.CharField(max_length=150)
    deks = models.TextField()
    
