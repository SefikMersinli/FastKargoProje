from django.contrib import admin
from .models import Kurye

@admin.register(Kurye)
class KuryeAdmin(admin.ModelAdmin):
    list_display = ('user', 'arac_tipi', 'müsait_mi', 'kayit_tarihi')
    list_filter = ('arac_tipi', 'müsait_mi')
    search_fields = ('user__username', 'telefon')