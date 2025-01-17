from django.urls import path
from . import views

urlpatterns = [
    path('', views.produk_list, name='produk_list'),  # URL untuk daftar produk
]