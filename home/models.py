from django.db import models

# Create your models here.
class Kaligrafi(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return "{}".format(self.title)
    