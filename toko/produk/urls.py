from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('produk/', views.produk_view, name='produk'),  # halaman daftar produk
    path('kontak/', views.kontak, name='kontak'), 
    path('tentang/', views.tentang, name='tentang'),
    path('produk/<int:product_id>/', views.product_detail, name='product_detail'), 
]