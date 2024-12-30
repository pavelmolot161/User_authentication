from django.shortcuts import render

### - 30.12.24

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django import forms
from Autent_App.models import *

### - представления Session-based Authentication:
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views import View

### - представления JWT
from rest_framework_simplejwt.views import TokenObtainPairView

### - представления для OAuth

#from social_django.utils import get_user_details
from social_core.pipeline.social_auth import social_details
from django.contrib.auth import login





### - представления Session-based Authentication:
class LoginView(View):
    def get(self, request):
        # Возвращаем HTML-форму для входа
        return render(request, 'login.html')  # Создайте файл login.html в папке templates

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        return JsonResponse({'message': 'Invalid credentials'}, status=400)

class LogoutView(View):
    def post(self, request):
        logout(request)
        return JsonResponse({'message': 'Logout successful'})

### -
class MyTokenObtainPairView(TokenObtainPairView):
    # Можно переопределить метод, если нужно
    pass

### - представления для OAuth
class GoogleLogin(View):
    def get(self, request):
        # Логика для обработки OAuth
        pass