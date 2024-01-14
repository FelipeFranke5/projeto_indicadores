import requests
from requests import Response
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authtoken.models import Token


class MainPageView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        base_url: str = settings.API_BASE_URL
        id_usuario: int = request.user.id
        token: str = Token.objects.get(user=request.user).key

        indicadores: Response = requests.get(
            url=f"{base_url}/api/indicadores/todos/{id_usuario}",
            timeout=3,
            headers={"AUTHORIZATION": f"Token {token}"},
        )

        if indicadores.status_code == 200:
            context = {"indicadores": indicadores.json}
            return render(request, "main.html", context)

        context = {"status_code": indicadores.status_code, "json": indicadores.json}
        return render(request, "http_erro.html", context)


class NovoIndicador(LoginRequiredMixin, View):
    raise_exception = True

    def post(self, request: HttpRequest) -> HttpResponse:
        base_url: str = settings.API_BASE_URL
        id_usuario: int = request.user.id
        token: str = Token.objects.get(user=request.user).key
        tmo = request.POST.get("tmo")
        aderencia = request.POST.get("aderencia")
        nps2 = request.POST.get("nps2")
        nps3 = request.POST.get("nps3")
        rechamada = request.POST.get("rechamada")
        shortcall = request.POST.get("shortcall")
        abst = request.POST.get("abs")
        transf_demais_ilhas = request.POST.get("transf_demais_ilhas")
        transf_pesquisa = request.POST.get("transf_pesquisa")

        indicador: Response = requests.post(
            url=f"{base_url}/api/indicadores/cadastrar/{id_usuario}/",
            headers={"AUTHORIZATION": f"Token {token}"},
            json={
                "tmo": tmo,
                "aderencia": aderencia,
                "nps2": nps2,
                "nps3": nps3,
                "rechamada": rechamada,
                "shortcall": shortcall,
                "abs": abst,
                "transf_demais_ilhas": transf_demais_ilhas,
                "transf_pesquisa": transf_pesquisa,
            },
            timeout=3,
        )

        if indicador.status_code == 201:
            return redirect(reverse("main:main"))

        context = {"status_code": indicador.status_code, "json": indicador.json}
        return render(request, "http_erro.html", context)


class NovaMeta(LoginRequiredMixin, View):
    raise_exception = True

    def post(self, request: HttpRequest) -> HttpResponse:
        base_url: str = settings.API_BASE_URL
        tmo = request.POST.get("tmo")
        aderencia = request.POST.get("aderencia")
        nps2 = request.POST.get("nps2")
        nps3 = request.POST.get("nps3")
        rechamada = request.POST.get("rechamada")
        shortcall = request.POST.get("shortcall")
        abst = request.POST.get("abs")
        transf_demais_ilhas = request.POST.get("transf_demais_ilhas")
        transf_pesquisa = request.POST.get("transf_pesquisa")

        meta: Response = requests.post(
            url=f"{base_url}/api/metas/cadastrar/",
            json={
                "tmo": tmo,
                "aderencia": aderencia,
                "nps2": nps2,
                "nps3": nps3,
                "rechamada": rechamada,
                "shortcall": shortcall,
                "abs": abst,
                "transf_demais_ilhas": transf_demais_ilhas,
                "transf_pesquisa": transf_pesquisa,
            },
            timeout=3,
        )

        if meta.status_code == 201:
            return redirect(reverse("main:main"))

        context = {"status_code": meta.status_code}
        return render(request, "http_erro.html", context)


# HTMX views abaixo


class ListaTodosIndicadores(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request: HttpRequest) -> HttpResponse:
        base_url: str = settings.API_BASE_URL
        id_usuario: int = request.user.id
        token: str = Token.objects.get(user=request.user).key

        indicadores: Response = requests.get(
            url=f"{base_url}/api/indicadores/todos/{id_usuario}",
            timeout=3,
            headers={"AUTHORIZATION": f"Token {token}"},
        )

        if indicadores.status_code == 200:
            context = {"indicadores": indicadores.json}
            return render(request, "lista_todos_indicadores.html", context)

        context = {"status_code": indicadores.status_code, "json": indicadores.json}
        return render(request, "http_erro.html", context)


class ListaTodosIndicadoresFechar(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('<div id="indicadores_todos"></div>')


class ListaTodasMetas(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request: HttpRequest) -> HttpResponse:
        base_url: str = settings.API_BASE_URL

        metas: Response = requests.get(url=f"{base_url}/api/metas/todos/", timeout=3)

        if metas.status_code == 200:
            context = {"metas": metas.json}
            return render(request, "lista_todas_metas.html", context)

        context = {
            "texto": metas.text,
            "status_code": metas.status_code,
        }
        return render(request, "http_erro.html", context)


class ListaTodasMetasFechar(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('<div id="metas_todos"></div>')


class FormCadastroIndicador(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "cadastro_indicador.html")


class FecharFormCadastroIndicador(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('<div id="form_cadastro_indicador"></div>')


class FormCadastroMeta(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "cadastro_meta.html")


class FecharFormCadastroMeta(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('<div id="form_cadastro_meta"></div>')
