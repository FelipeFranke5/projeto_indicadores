from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import (
    MinimumLengthValidator,
    CommonPasswordValidator,
    NumericPasswordValidator,
)
from django.views.decorators.http import require_http_methods
from .forms import CadastroUsuario
from .validacoes import ValidacaoNomeUsuario, ValidacaoSenha1, ValidacaoSenha2


@require_http_methods(["GET", "POST"])
def cadastro(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect(reverse("main:main"))
    if request.method == "POST":
        form = CadastroUsuario(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect(reverse("main:main"))
        return render(request, "registration/cadastro.html", {"form": form})
    form = CadastroUsuario()
    return render(request, "registration/cadastro.html", {"form": form})


# HTMX views abaixo


@require_http_methods(["POST"])
def validar_senha2(request: HttpRequest) -> HttpResponse:
    validacao = ValidacaoSenha2(request)

    if not validacao.senha2_esta_vazia():
        senha2_obrigatorio = '<li class="list-group-item fw-light list-group-item-primary" \
id="senha2_obrigatorio"><small>Campo preenchido.</small></li>'
    else:
        senha2_obrigatorio = '<li class="list-group-item fw-light list-group-item-danger" \
id="senha2_obrigatorio"><small>Preencha esse campo.</small></li>'

    if validacao.senha2_igual_senha1():
        senha2_igual = '<li class="list-group-item fw-light list-group-item-primary" \
id="senha2_igual"><small>As senhas são iguais.</small></li>'
    else:
        senha2_igual = '<li class="list-group-item fw-light list-group-item-danger" \
id="senha2_igual"><small>Preencha a mesma senha nos dois campos.</small></li>'

    listas = {
        "senha2_obrigatorio": senha2_obrigatorio,
        "senha2_igual": senha2_igual,
    }
    return render(request, "registration/htmx_templates/senha2.html", listas)


@require_http_methods(["POST"])
def validar_senha1(request: HttpRequest) -> HttpResponse:
    validacao = ValidacaoSenha1(request)

    if not validacao.senha1_esta_vazia():
        senha1_obrigatorio = '<li class="list-group-item fw-light list-group-item-primary" \
id="senha1_obrigatorio"><small>Campo preenchido.</small></li>'
    else:
        senha1_obrigatorio = '<li class="list-group-item fw-light list-group-item-danger" \
id="senha1_obrigatorio"><small>Preencha esse campo.</small></li>'

    if not validacao.senha1_excede_caracteres():
        senha1_max = '<li class="list-group-item fw-light list-group-item-primary" \
id="senha1_max"><small>Campo dentro do limite máximo de caracteres.</small></li>'
    else:
        senha1_max = '<li class="list-group-item fw-light list-group-item-danger" \
id="senha1_max"><small>Preencha no máximo 128 caracteres.</small></li>'

    if not validacao.senha1_semelhante_usuario():
        senha1_usuario = '<li class="list-group-item fw-light list-group-item-primary" \
id="senha1_usuario"><small>Não é parecido com o Nome de Usuário.</small></li>'
    else:
        senha1_usuario = '<li class="list-group-item fw-light list-group-item-danger" \
id="senha1_usuario"><small>Defina uma senha que não se pareça com o Nome de Usuário.</small></li>'

    try:
        MinimumLengthValidator().validate(validacao.obter_senha1())
        senha1_min = '<li class="list-group-item fw-light list-group-item-primary" \
id="senha1_min"><small>Possui mais de 8 caracteres.</small></li>'
    except ValidationError:
        senha1_min = '<li class="list-group-item fw-light list-group-item-danger" \
id="senha1_min"><small>Digite ao menos 8 caracteres.</small></li>'

    try:
        CommonPasswordValidator().validate(validacao.obter_senha1())
        senha1_com = '<li class="list-group-item fw-light list-group-item-primary" \
id="senha1_com"><small>Não é muito comum.</small></li>'
    except ValidationError:
        senha1_com = '<li class="list-group-item fw-light list-group-item-danger" \
id="senha1_com"><small>Defina uma senha mais única.</small></li>'

    try:
        NumericPasswordValidator().validate(validacao.obter_senha1())
        senha1_numerica = '<li class="list-group-item fw-light list-group-item-primary" \
id="senha1_numerica"><small>Contém letras e números.</small></li>'
    except ValidationError:
        senha1_numerica = '<li class="list-group-item fw-light list-group-item-danger" \
id="senha1_numerica"><small>Digite letras e números.</small></li>'

    listas = {
        "senha1_obrigatorio": senha1_obrigatorio,
        "senha1_min": senha1_min,
        "senha1_max": senha1_max,
        "senha1_usuario": senha1_usuario,
        "senha1_numerica": senha1_numerica,
        "senha1_com": senha1_com,
    }
    return render(request, "registration/htmx_templates/senha1.html", listas)


@require_http_methods(["POST"])
def validar_nome_usuario(request: HttpRequest) -> HttpResponse:
    validacao = ValidacaoNomeUsuario(request)

    if not validacao.usuario_esta_vazio():
        campo_obrigatorio = '<li class="list-group-item list-group-item-primary \
fw-light" id="campo_obrigatorio"><small>Campo preenchido.</small></li>'
    else:
        campo_obrigatorio = '<li class="list-group-item list-group-item-danger \
fw-light" id="campo_obrigatorio"><small>Preencha esse campo.</small></li>'

    if not validacao.usuario_excede_caracteres():
        campo_max_150 = '<li class="list-group-item list-group-item-primary fw-light" \
id="campo_max_150"><small>Está dentro do limite de 150 caracteres.</small></li>'
    else:
        campo_max_150 = '<li class="list-group-item list-group-item-danger fw-light" \
    id="campo_max_150"><small>Campo excedeu o máximo de caracteres.</small></li>'

    if not validacao.usuario_nao_tem_minimo_recomendado():
        campo_min_5 = '<li class="list-group-item list-group-item-primary fw-light" \
id="campo_min_5"><small>Possui no mínimo 5 caracteres.</small></li>'
    else:
        campo_min_5 = '<li class="list-group-item list-group-item-warning fw-light" \
id="campo_min_5"><small>Opcional: Digite ao menos 5 caracteres.</small></li>'

    if (
        validacao.usuario_possui_caracteres_permitidos()
        and not validacao.usuario_possui_caracteres_nao_permitidos()
    ):
        campo_espec = '<li class="list-group-item list-group-item-primary fw-light" \
id="campo_espec"><small>Possui caracteres especiais permitidos.</small></li>'
    else:
        campo_espec = '<li class="list-group-item list-group-item-warning fw-light" \
id="campo_espec"><small>Opcional: Deve conter (apenas) os caracteres especiais @/./+/-/_.</small></li>'

    if not validacao.usuario_possui_caracteres_nao_permitidos():
        campo_espec1 = '<li class="list-group-item list-group-item-primary fw-light" \
id="campo_espec"><small>Não possui caracteres não permitidos.</small></li>'
    else:
        campo_espec1 = '<li class="list-group-item list-group-item-danger fw-light" \
id="campo_espec"><small>Retire os caracteres !#$%¨&*().</small></li>'

    if validacao.usuario_alfanumerico():
        campo_alfanum = '<li class="list-group-item fw-light list-group-item-primary" \
id="campo_alfanum"><small>Campo é alfanumérico.</small></li>'
    else:
        campo_alfanum = '<li class="list-group-item fw-light list-group-item-warning" \
id="campo_alfanum"><small>Digite letras e números.</small></li>'

    try:
        User.objects.get(username=validacao.obter_usuario())
        usuario_exis = '<li class="list-group-item fw-light list-group-item-danger" \
id="usuario_exis"><small>Já existe um usuário com esse nome.</small></li>'
    except User.DoesNotExist:
        usuario_exis = '<li class="list-group-item fw-light list-group-item-primary" \
id="usuario_exis"><small>Nome de Usuário válido.</small></li>'

    listas = {
        "usuario_exis": usuario_exis,
        "campo_obrigatorio": campo_obrigatorio,
        "campo_min_5": campo_min_5,
        "campo_max_150": campo_max_150,
        "campo_alfanum": campo_alfanum,
        "campo_espec": campo_espec,
        "campo_espec1": campo_espec1,
    }
    return render(request, "registration/htmx_templates/usuario.html", listas)
