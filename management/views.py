from django.shortcuts import render

def admin_dashboard(request):
    # Şu anlık hiçbir veri yok, sadece tasarım gösteriliyor
    return render(request, 'dashboard.html', {})
