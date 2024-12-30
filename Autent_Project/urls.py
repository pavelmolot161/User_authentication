"""
URL configuration for Autent_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

### - маршруты для Session-based Authentication:
from django.contrib import admin
from django.urls import path
from Autent_App.views import LoginView, LogoutView

### - маршруты для JWT:
from rest_framework_simplejwt.views import TokenRefreshView
from Autent_App.views import MyTokenObtainPairView

### - маршруты для OAuth:
from Autent_App.views import GoogleLogin


urlpatterns = [
    path('admin/', admin.site.urls),

### - маршруты для Session-based Authentication:
    path('', LoginView.as_view(), name='login'), ### - маршруты для Session-based Authentication:
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  ### - маршруты для JWT:
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('auth/google/', GoogleLogin.as_view(), name='google_login'),                   ### - маршруты для OAuth:
]

