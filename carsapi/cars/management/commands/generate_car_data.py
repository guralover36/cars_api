from django.core.management.base import BaseCommand
from faker import Faker
from cars.models import Car, Brand, Marka
from cars.models import BODY_STYLES, FUEL_TYPES, TRANSMISSION_TYPES

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()

        # Generate fake data and save to the database
        for _ in range(10):
            manufacturer = fake.company()
            model = fake.random_element(elements=('SUV', 'Sedan', 'Hatchback', 'Convertible'))
            year = fake.year()
            color = fake.color_name()
            color2 = fake.color_name()
            price = fake.random_number(digits=5)

            marka, created = Marka.objects.get_or_create(
                name=model,
                age_of_issue=year,
                style=fake.random_choices(elements=BODY_STYLES)
            )

            brand, created = Brand.objects.get_or_create(
                name=manufacturer,
                country=fake.country()
            )

            car = Car.objects.create(
                brand=brand,
                marka=marka,
                price=price,
                mileage=fake.random_number(digits=5),
                exterior_color=color,
                interior_color=color2,
                fuel_type=fake.random_element(elements=FUEL_TYPES),
                transmission=fake.random_element(elements=TRANSMISSION_TYPES),
                engine=fake.random_element(elements=('V6', 'V8', 'V12')),
                sale=fake.random_element(elements=(True, False))
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated fake car data'))
