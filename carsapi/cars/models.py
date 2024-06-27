from django.db import models
from django.contrib.auth.models import AbstractUser, Group


# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)


class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Marka(models.Model):
    name = models.CharField(max_length=100)
    age_of_issue = models.IntegerField()
    style = models.CharField(max_length=100)


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    price = models.IntegerField()
    mileage = models.IntegerField()
    # change oe approve
    exterior_color = models.CharField(max_length=100)
    interior_color = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    sale = models.BooleanField()



