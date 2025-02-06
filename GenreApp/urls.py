from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('',genre_homepage,name="genreHomepage")
]