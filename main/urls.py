from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('', indexHandler),
    path('sport/', sportHandler)
]