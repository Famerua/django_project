from django.contrib import admin
from django.urls import path

from .views import get_movies, get_the_movie

# fmt:off
urlpatterns = [
    path("", get_movies),
    path('<int:pk>', get_the_movie)
]
