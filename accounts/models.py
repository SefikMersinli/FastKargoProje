from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AccountManager(models.Manager):
    def register(self, username, email, password1, password2):
        if not username or not email or not password1 or not password2:
            raise ValidationError("Tüm alanları doldurun.")

        if password1 != password2:
            raise ValidationError("Şifreler uyuşmuyor.")

        if User.objects.filter(username=username).exists():
            raise ValidationError("Bu kullanıcı adı zaten kullanılıyor.")

        if User.objects.filter(email=email).exists():
            raise ValidationError("Bu e-posta zaten kayıtlı.")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        self.create(user=user)
        return user


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = AccountManager()

    def __str__(self):
        return self.user.username
