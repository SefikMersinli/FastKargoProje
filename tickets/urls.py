# tickets/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Müşteri view'ları
    path('listele/', views.ticket_list, name='ticket_list'),
    path('olustur/', views.ticket_create, name='ticket_create'),
    path('<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    
    # Yönetici view'ları (opsiyonel, listelemeyi zaten dashboard'da yaptık)
]