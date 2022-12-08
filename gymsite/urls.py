"""gymsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gymapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.Index, name='Home'),
    path('about-us/',views.AboutUs, name='About'),
    path('blog/',views.Blog, name='Blog'),
    path('blog-details/',views.BlogDetails, name='BlogDetails'),
    path('contact/',views.Contact, name='Contact'),
    path('gallery/',views.Gallery, name='Gallery'),
    path('services/',views.Services, name='Services'),
    path('team/',views.Team, name='Team'),
    path('class-details/',views.ClassDetails, name='ClassDetails'),
    path('class-timetable/',views.ClassTimetable, name='ClassTimetable'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
