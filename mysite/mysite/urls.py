from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('C:\Users\yummy\PycharmProjects\mysite\members', include('members.urls')),
    path('C:\Users\yummy\PycharmProjects\mysite\members\admin.py', admin.site.urls),
]