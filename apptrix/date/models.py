from django.db import models

# Create your models here.
class Person(models.Model):
    img = models.ImageField()
    gender = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()