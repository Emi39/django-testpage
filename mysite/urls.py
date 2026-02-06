from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render  # if using templates

def home(request):
    return HttpResponse("""
    <h1>Hello from Vanja's site on Koyeb! 🚀</h1>
    <p>Running Django 6.0</p>
    <ul>
        <li><a href="/about/">About me</a></li>
        <li><a href="/contact/">Contact</a></li>
    </ul>
    """)

def about(request):
    return HttpResponse("<h1>About Vanja</h1><p>I live in Portage la Prairie, Manitoba, and I'm learning Django + deployment!</p>")

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    # path('admin/', admin.site.urls),
]