from django.contrib import admin
from cars.models import Marka, Car, Brand, CustomUser

# Register your models here.
admin.site.register(Marka)
admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(CustomUser)
