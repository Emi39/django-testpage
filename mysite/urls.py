from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render  # if using templates

def home(request):
    
    return render(request, 'home.html', {'title': "Vanja's Site"})
 

def about(request):
    return HttpResponse("<h1>About Vanja</h1><p>I live in Portage la Prairie, Manitoba, and I'm learning Django + deployment!</p>")

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    # path('admin/', admin.site.urls),
]