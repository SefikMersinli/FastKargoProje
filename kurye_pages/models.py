from django.db import models
from django.contrib.auth.models import User

class Kurye(models.Model):
    # Kuryeyi bir kullanıcıya bağlıyoruz
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Kullanıcı")
    
    # Kuryeye özel bilgiler
    telefon = models.CharField(max_length=15, verbose_name="Telefon Numarası")
    arac_tipi = models.CharField(max_length=50, choices=[
        ('Motor', 'Motosiklet'),
        ('Araba', 'Hafif Ticari'),
        ('Yaya', 'Yaya Kurye')
    ], default='Motor', verbose_name="Araç Tipi")
    
    müsait_mi = models.BooleanField(default=True, verbose_name="Çalışmaya Hazır mı?")
    kayit_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.arac_tipi}"

    class Meta:
        verbose_name = "Kurye"
        verbose_name_plural = "Kuryeler"