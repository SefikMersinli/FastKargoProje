from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Cargo, CargoHistory
# Sefik tarafından güncellendi
# Son guncelleme Sefik

@login_required
def cargo_list(request):
    """Sadece kullanıcıya özel kargo listeleme ve filtreleme."""
  
    kargolar = Cargo.objects.filter(user=request.user).order_by('-olusturma')

    
    query = request.GET.get('q')
    durum_filtresi = request.GET.get('durum')
    tarih_filtresi = request.GET.get('tarih')
    
   
    if query:
        kargolar = kargolar.filter(
            Q(takip_no__icontains=query) | 
            Q(alici__icontains=query)
        )
    
   
    if durum_filtresi:
        kargolar = kargolar.filter(durum=durum_filtresi)
        
   
    if tarih_filtresi:
        kargolar = kargolar.filter(olusturma__date=tarih_filtresi)

    return render(request, 'cargo_list.html', {'kargolar': kargolar})

@login_required
def cargo_create(request):
    if request.method == "POST":
       
        agirlik_verisi = request.POST.get('agirlik')
        agirlik = float(agirlik_verisi) if agirlik_verisi and agirlik_verisi != '' else 1.0
        
       
        
        hesaplanan_fiyat = 60 + (agirlik * 25)

        yeni_kargo = Cargo.objects.create(
            user=request.user,
            gonderen_ad=request.POST.get('gonderen_ad'),
            gonderen_tel=request.POST.get('gonderen_tel'),
            gonderen_adres=request.POST.get('gonderen_adres'),
            alici=request.POST.get('alici'),
            alici_tel=request.POST.get('alici_tel'),
            adres=request.POST.get('alici_adres'),
            gonderi_turu=request.POST.get('gonderi_turu'),
            agirlik=agirlik,
            odeme_turu=request.POST.get('odeme_turu'),
            aciklama=request.POST.get('aciklama'),
            fiyat=hesaplanan_fiyat, # İşte burası dinamik oldu!
            durum='YOLDA'
        )
        
     
        CargoHistory.objects.create(
            cargo=yeni_kargo,
            konum="Gönderi Kabul Edildi",
            detay=f"Kargonuz {agirlik} kg olarak tartıldı ve işleme alındı."
        )
        
        messages.success(request, f"Kargo başarıyla oluşturuldu! Takip No: {yeni_kargo.takip_no} | Ücret: {hesaplanan_fiyat} ₺")
        return redirect('cargo_list')
    
    return render(request, 'cargo_create.html')

def cargo_info(request, takip_no):
    """Kargo detay sayfası (Herkes takip no ile bakabilir)."""
    try:
        kargo = Cargo.objects.get(takip_no=takip_no)
        return render(request, 'cargo_info.html', {'kargo': kargo})
    except Cargo.DoesNotExist:
        messages.error(request, f"'{takip_no}' takip numaralı bir kargo bulunamadı.")
        return redirect('home')   