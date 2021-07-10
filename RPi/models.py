from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.CharField(max_length=10000000)
    date = models.CharField(max_length=100, unique=False)
    processed = models.BooleanField()


class Flag(models.Model):
    image_flag = models.CharField(max_length=50)

