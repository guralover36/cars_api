from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import MaxValueValidator


BODY_STYLES = (
    ("sedan", "Sedan"),
    ("hatchback", "HatchBack"),
    ("liftback", "Liftback"),
    ("coupe", "Coupe"),
    ("crossover", "Crossover"),
    ("truck", "Truck"),
    ("wagon", "Wagon"),
)

FUEL_TYPES = (
    ("gasoline", "Gasoline"),
    ("diesel", "Diesel"),
    ("biodiesel", "Biodiesel"),
    ("ethanol", "Ethanol"),
    ("cng", "CNG"),
    ("lpg", "LPG"),
    ("hydrogen", "Hydrogen"),
)

TRANSMISSION_TYPES = (
    ("manual", "Manual"),
    ("automatic", "Automatic"),
    ("cvt", "CVT"),
    ("semi-automatic", "Semi-Automatic"),
)

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)


class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Marka(models.Model):
    name = models.CharField(max_length=100)
    age_of_issue = models.IntegerField(blank=False, null=False, validators=[MaxValueValidator(2050)])
    style = models.CharField(blank=False, null=False, choices=BODY_STYLES, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Marka"
        verbose_name_plural = "Markas"


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    price = models.IntegerField()
    mileage = models.IntegerField()
    # change oe approve
    exterior_color = models.CharField(max_length=100)
    interior_color = models.CharField(max_length=100)
    fuel_type = models.CharField(blank=False, null=False, choices=FUEL_TYPES, max_length=30)
    transmission = models.CharField(blank=False, null=False, choices=TRANSMISSION_TYPES, max_length=50)
    engine = models.CharField(max_length=100)
    sale = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return f"{self.brand}: {self.marka}"


    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"



