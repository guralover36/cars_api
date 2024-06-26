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
    age_of_issue = models.IntegerField(max_length=4)
    style = models.CharField(max_length=100)


class Car(models.Model):
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE)
    marka = models.OneToOneField(Marka, on_delete=models.CASCADE)
    price = models.IntegerField(max_length=10)
    mileage = models.IntegerField()
    # change oe approve
    exterior_color = models.JSONField(default=list)
    interior_color = models.JSONField(default=list)
    fuel_type = models.JSONField(default=list)
    transmission = models.JSONField(default=list)
    engine = models.CharField()
    sale = models.BooleanField()



admin_group, created = Group.objects.get_or_create(name='Administrators')
registered_group, created = Group.objects.get_or_create(name='Registered Users')
guest_group, created = Group.objects.get_or_create(name='Guest Users')