from django.db import models
import uuid

class Cargo(models.Model):
    # Girinti hatası düzeltildi
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Kullanıcı")
    
    DURUM_CHOICES = [
        ('YOLDA', 'Yolda / İşleniyor'),
        ('DAGITIMDA', 'Dağıtımda'),
        ('TESLIM', 'Teslim Edildi'),
    ]
    
    takip_no = models.CharField(max_length=20, unique=True, editable=False)
    gonderen_ad = models.CharField(max_length=100)
    gonderen_tel = models.CharField(max_length=20)
    gonderen_adres = models.TextField()
    
    alici = models.CharField(max_length=100)
    alici_tel = models.CharField(max_length=20)
    adres = models.TextField()
    
    gonderi_turu = models.CharField(max_length=50)
    agirlik = models.FloatField()
    odeme_turu = models.CharField(max_length=50)
    aciklama = models.TextField(blank=True, null=True)
    
    fiyat = models.DecimalField(max_digits=10, decimal_places=2, default=150.00)
    durum = models.CharField(max_length=20, choices=DURUM_CHOICES, default='YOLDA')
    olusturma = models.DateTimeField(auto_now_add=True)
    guncelleme = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.takip_no:
            self.takip_no = "FK" + str(uuid.uuid4().hex[:9]).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.takip_no

class CargoHistory(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='gecmis')
    konum = models.CharField(max_length=255)
    detay = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-tarih']