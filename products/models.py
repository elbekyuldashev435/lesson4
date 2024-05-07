from django.db import models

# Create your models here.


class Cars(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=100)
