from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from voting import views   # ✅ ADD THIS

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home),  # HOME FIRST
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),  # ✅ NOW WORKS
]