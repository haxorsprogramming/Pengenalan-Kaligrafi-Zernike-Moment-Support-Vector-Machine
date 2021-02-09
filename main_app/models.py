from django.db import models

# Create your models here.
class Class_Kaligrafi(models.Model):
    kd = models.CharField(max_length=150)
    nama = models.CharField(max_length=150)
    deks = models.TextField()
    
class Nilai_Data_Latih(models.Model):
    kd_class = models.CharField(max_length=150)
    node = models.IntegerField()
    value = models.FloatField()

class Pengujian_Citra(models.Model):
    kd_uji = models.CharField(max_length=50)
    nama_pengujian = models.CharField(max_length=150)
    waktu_pengujian = models.DateTimeField()
    base_svm_final = models.FloatField()
    hasil_final = models.CharField(max_length=150)
