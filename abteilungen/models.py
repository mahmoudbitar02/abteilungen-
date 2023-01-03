from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class abteilungen(models.Model):
    titel = models.CharField(max_length=50)
    content = models.TextField(max_length=10000)
    image = models.ImageField('abteilung1/')
    author = models.ForeignKey(User, related_name='abteiung_author' ,on_delete=models.CASCADE )


    def __str__(self):
        return self.titel