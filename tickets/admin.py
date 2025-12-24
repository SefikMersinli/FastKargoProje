from django.contrib import admin
from .models import Ticket, TicketMessage

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    # Murat'ın modelindeki gerçek isimleri buraya yazdım:
    list_display = ('id', 'konu', 'isim', 'durum', 'olusturma')
    list_filter = ('durum', 'konu')
    search_fields = ('isim', 'email', 'mesaj')

@admin.register(TicketMessage)
class TicketMessageAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'is_admin', 'olusturma')