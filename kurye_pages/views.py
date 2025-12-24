from django.shortcuts import render

def home(request):
    # Burası Yusuf'un kurye panelini açar. 
    # templates içinde 'kurye_home.html' olduğundan emin ol!
    return render(request, 'kurye_home.html') 

def login_view(request):
    return render(request, 'kurye_login.html')

def register_view(request):
    return render(request, 'kurye_register.html')