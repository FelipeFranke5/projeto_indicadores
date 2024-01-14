from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django_recaptcha.fields import ReCaptchaField


class CadastroUsuario(UserCreationForm):
    recaptcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "recaptcha"]
