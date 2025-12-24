from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='kurye_dashboard'),        
    path('giris/', views.login_view, name='kurye_login'),
    path('kayit/', views.register_view, name='kurye_register'),
]