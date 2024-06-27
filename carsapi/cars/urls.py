from django.urls import path
from .views import register, login_view, home
# from django.contrib.auth import views as auth_views
# from .forms import CustomUserLoginForm

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
]