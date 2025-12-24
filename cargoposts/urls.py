from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargo_list, name='cargo_list'),
    path('olustur/', views.cargo_create, name='cargo_create'),
    path('<str:takip_no>/', views.cargo_info, name='cargo_info'),
]