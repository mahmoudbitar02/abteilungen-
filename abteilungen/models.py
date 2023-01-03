from django.db import models

# Create your models here.


class abteilungen(models.Model):
    titel = models.CharField(max_length=50)
    content = models.TextField(max_length=10000)
    