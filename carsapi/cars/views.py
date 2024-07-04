from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserRegistrationForm, CustomUserLoginForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from cars.serializers import UserLoginSerializer
from cars.serializers import UserRegistrationSerializer
from django.contrib.auth import login
from cars.serializers import *


# Create your views here.
class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)  # Automatically log in the user after registration
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    return render(request, 'home.html')

class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#api
class BrandApiView(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        if name:
            brands = Brand.objects.filter(name__exact=name)
        else:
            brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

class MarkaApiView(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        if name:
            markas = Marka.objects.filter(name__exact=name)
        else:
            markas = Marka.objects.all()
        serializer = MarkaSerializer(markas, many=True)
        return Response(serializer.data)

class CarOnSaleApiView(APIView):
    def get(self, request):
        cars_on_sale = Car.objects.filter(sale=True)
        serializer = CarSerializer(cars_on_sale, many=True)
        return Response(serializer.data)

class CarApiView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        print(serializer.data)
        return Response(serializer.data)