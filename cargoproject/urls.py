from django.contrib import admin
from django.urls import path, include
from . import views # Ana dizindeki views (Ömer'in vitrini için)

urlpatterns = [
    path('', views.home, name="home"),               
    path('accounts/', include('accounts.urls')),
    path('kargolar/', include('cargoposts.urls')),      
    path('dashboard/', include('management.urls')),
    path('admin/', admin.site.urls),
    path('tickets/', include('tickets.urls')),
    path('kurye-panel/', include('kurye_pages.urls')), 
]