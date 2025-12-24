
from django.shortcuts import render, redirect
from datetime import datetime, timedelta

SAHTE_TICKETLAR = [
    {
        'id': 1001,
        'konu': 'Teslimat Sorunu',
        'email': 'ahmet@mail.com',
        'mesaj': 'Kargomun durumu günlerdir değişmiyor.',
        'durum': 'Açık',
        'olusturma': datetime.now() - timedelta(hours=8),
        'cevaplar': [
            {'mesaj': 'Kargomun durumu günlerdir değişmiyor.', 'gonderen': 'musteri', 'tarih': datetime.now() - timedelta(hours=7)},
            {'mesaj': 'Talebiniz alınmıştır. Operasyon ekibimiz kontrol ediyor.', 'gonderen': 'yonetici', 'tarih': datetime.now() - timedelta(hours=5)},
            {'mesaj': 'Bekliyorum.', 'gonderen': 'musteri', 'tarih': datetime.now() - timedelta(hours=4)},
        ]
    },
    {
        'id': 1002,
        'konu': 'İade/Değişim Talebi',
        'email': 'ayse@mail.com',
        'mesaj': 'Ürün hasarlı geldiği için iade etmek istiyorum.',
        'durum': 'Yanıt Bekleniyor',
        'olusturma': datetime.now() - timedelta(days=1),
        'cevaplar': [
            {'mesaj': 'Ürün hasarlı geldiği için iade etmek istiyorum.', 'gonderen': 'musteri', 'tarih': datetime.now() - timedelta(hours=23)},
            {'mesaj': 'İade formunuzu doldurup bize gönderebilir misiniz?', 'gonderen': 'yonetici', 'tarih': datetime.now() - timedelta(hours=20)},
        ]
    },
]


def ticket_list(request):
    """ Tüm ticketları listeler (Prototip). """
    context = {'ticketlar': SAHTE_TICKETLAR}
    return render(request, 'ticket_list.html', context) 

def ticket_create(request):
    """ Ticket oluşturma formunu gösterir ve form gönderme işlemini simüle eder. """
    
    if request.method == 'POST':
        return redirect('ticket_list') 

    initial_data = {}
    if request.user.is_authenticated:
        initial_data['isim'] = request.user.get_full_name() or request.user.username
        initial_data['email'] = request.user.email
    
    return render(request, 'ticket_create.html', {'initial': initial_data}) 

def ticket_detail(request, ticket_id):
    """ Ticket detayını ve mesaj balonlarını gösterir. """
    try:
        ticket_id = int(ticket_id) 
        ticket = next(t for t in SAHTE_TICKETLAR if t['id'] == ticket_id)
    except (StopIteration, ValueError):
        return redirect('ticket_list')
        
    context = {'ticket': ticket, 'is_staff': False} 
    return render(request, 'ticket_detail.html', context) 