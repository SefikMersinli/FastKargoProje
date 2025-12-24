from django.contrib import admin
from .models import Cargo, CargoHistory


class CargoHistoryInline(admin.TabularInline):
    model = CargoHistory
    extra = 1

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
   
    list_display = ('takip_no', 'user', 'alici', 'durum', 'olusturma')
 
    list_filter = ('durum', 'olusturma', 'user')

    search_fields = ('takip_no', 'alici', 'gonderen_ad')
   
    inlines = [CargoHistoryInline]


admin.site.register(CargoHistory)