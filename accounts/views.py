from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import Account

def register_view(request):
    if request.method == "POST":
        data = request.POST
        p1 = data.get("password1")
        p2 = data.get("password2")
        try:
            if p1 != p2:
                raise ValidationError("Şifreler uyuşmuyor dostum!")
            
            validate_password(p1) # Zayıf şifre kontrolü

            user = Account.objects.register(
                data.get("username"),
                data.get("email"),
                p1,
                p2,
            )
            login(request, user)
            return redirect("home")
        except ValidationError as e:
            msg = e.messages[0] if hasattr(e, 'messages') else str(e)
            return render(request, "register.html", {"error": f"Biraz zayıf dostum! {msg}"})
        except Exception as e:
            return render(request, "register.html", {"error": f"Hata: {str(e)}"})
    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        u_name = request.POST.get("username")
        u_pass = request.POST.get("password")
        user = authenticate(request, username=u_name, password=u_pass)
        if user is not None:
            login(request, user)
            return redirect("home")
        return render(request, "login.html", {"error": "Kullanıcı adı veya şifre hatalı dostum!"})
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")