from django.urls import path, include
from . import views

app_name = "accounts"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("cadastro/", views.cadastro, name="cadastro"),
]

# HTMX
htmx_urlpatterns = [
    path("senha1/", views.validar_senha1, name="vld_sn1"),
    path("senha2/", views.validar_senha2, name="vld_sn2"),
    path("usuario/", views.validar_nome_usuario, name="vld_usr"),
]

urlpatterns += htmx_urlpatterns
