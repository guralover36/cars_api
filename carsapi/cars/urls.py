from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, BrandApiView, MarkaApiView, CarOnSaleApiView, CarApiView
# from django.contrib.auth import views as auth_views
# from .forms import CustomUserLoginForm
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    # path('home/', home, name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('brands/', BrandApiView.as_view(), name='brand'),
    path('marka/', MarkaApiView.as_view(), name='marka'),
    path('car/', CarApiView.as_view(), name='car'),
    path('caronsale/', CarOnSaleApiView.as_view(), name='caronsale')
]
