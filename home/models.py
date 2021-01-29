from django.db import models

# Create your models here.
class Kaligrafi(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return "{}".format(self.title)

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=150)
    nama = models.CharField(max_length=150)
    alamat = models.CharField(max_length=150)
    prodi = models.CharField(max_length=150)