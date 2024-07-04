from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from cars.models import Brand, Marka, CustomUser, Car

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            name=validated_data['name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class BrandSerializer(serializers.Serializer):
    class Meta:
        model = Brand
        fields = ('name', 'country')
    name = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    
class MarkaSerializer(serializers.Serializer):
    class Meta:
        model = Marka
        fields = ('name', 'age_of_issue', 'style')
    name = serializers.CharField(max_length=100)
    age_of_issue = serializers.IntegerField()
    style = serializers.CharField(max_length=100)

class CarSerializer(serializers.Serializer):
    class Meta:
        model = Car
        fields = ('brand', 'marka', 'price', 'mileage', 'exterior_color', 'interior_color', 'fuel_type', 'transmission', 'engine', 'sale')
    brand = serializers.CharField(max_length=100)
    marka = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    mileage = serializers.IntegerField()
    exterior_color = serializers.CharField(max_length=100)
    interior_color = serializers.CharField(max_length=100)
    fuel_type = serializers.CharField(max_length=30)
    transmission = serializers.CharField(max_length=50)
    engine = serializers.CharField(max_length=100)
    sale = serializers.BooleanField()
