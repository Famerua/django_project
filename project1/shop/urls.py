from django.contrib import admin
from django.urls import path

from .views import get_index_page, get_product_details

urlpatterns = [
    path("", get_index_page),
    path("<int:primary_key>", get_product_details),
]
