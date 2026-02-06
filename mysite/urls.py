from django.contrib import admin
from django.urls import path
from django.http import HttpResponse  # For quick test

def home(request):
    return HttpResponse("<h1>Hello from Vanja's site on Koyeb! 🚀</h1><p>Running Django 6.0</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Root URL '/'
]