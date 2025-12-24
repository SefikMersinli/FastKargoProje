# tickets/models.py
from django.db import models
from django.utils import timezone

# -- Seçenekler --

KONU_SECENEKLERI = [
    ('GECIKME', 'Teslimat Gecikmesi'),
    ('HASAR', 'Hasarlı Gönderi'),
    ('FIYAT', 'Fiyatlandırma Sorunu'),
    ('DIGER', 'Diğer'),
]

DURUM_SECENEKLERI = [
    ('ACIK', 'Açık'),
    ('BEKLEMEDE', 'Beklemede'),
    ('KAPALI', 'Kapalı'),
]


# --- Model 1: Ticket (Destek Talebi) ---

class Ticket(models.Model):
    konu = models.CharField(
        max_length=10, 
        choices=KONU_SECENEKLERI, 
        default='DIGER', 
        verbose_name="Talep Konusu"
    )
    durum = models.CharField(
        max_length=10, 
        choices=DURUM_SECENEKLERI, 
        default='ACIK', 
        verbose_name="Ticket Durumu"
    )
    
    # İletişim Bilgileri (Giriş yapmamış kullanıcı da kullanabilir)
    isim = models.CharField(max_length=100, verbose_name="İsim Soyisim")
    email = models.EmailField(verbose_name="E-posta Adresi")
    mesaj = models.TextField(verbose_name="Talep İçeriği") # İlk mesaj
    
    olusturma = models.DateTimeField(default=timezone.now, verbose_name="Oluşturulma Tarihi")
    
    class Meta:
        verbose_name = "Destek Talebi (Ticket)"
        verbose_name_plural = "Destek Talepleri (Ticket)"
        ordering = ['-olusturma']
        
    def __str__(self):
        return f"Ticket #{self.id} - {self.get_konu_display()}"


# --- Model 2: TicketMessage (Destek Mesajları) ---

class TicketMessage(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='mesajlar', verbose_name="Ticket")
    
    # Mesajı gönderen kişi admin mi (True) yoksa müşteri mi (False)
    is_admin = models.BooleanField(default=False, verbose_name="Yönetici Mesajı")
    
    icerik = models.TextField(verbose_name="Mesaj İçeriği")
    olusturma = models.DateTimeField(default=timezone.now, verbose_name="Gönderim Tarihi")
    
    class Meta:
        verbose_name = "Ticket Mesajı"
        verbose_name_plural = "Ticket Mesajları"
        ordering = ['olusturma'] 

    def __str__(self):
        return f"Mesaj #{self.pk} ({self.ticket.id})"