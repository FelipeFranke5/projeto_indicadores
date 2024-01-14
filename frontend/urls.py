from django.urls import path
from .views import (
    MainPageView,
    ListaTodosIndicadores,
    ListaTodosIndicadoresFechar,
    ListaTodasMetas,
    ListaTodasMetasFechar,
    NovoIndicador,
    NovaMeta,
    FormCadastroIndicador,
    FecharFormCadastroIndicador,
    FormCadastroMeta,
    FecharFormCadastroMeta,
)


app_name = "main"
urlpatterns = [
    path("", MainPageView.as_view(), name="main"),
    path("novo_indicador/", NovoIndicador.as_view(), name="novo_indicador"),
    path("nova_meta/", NovaMeta.as_view(), name="nova_meta"),
]


htmx_urls = [
    path(
        "todos_indicadores/", ListaTodosIndicadores.as_view(), name="todos_indicadores"
    ),
    path(
        "todos_indicadores_fechar/",
        ListaTodosIndicadoresFechar.as_view(),
        name="todos_indicadores_fechar",
    ),
    path(
        "todas_metas/",
        ListaTodasMetas.as_view(),
        name="todas_metas",
    ),
    path(
        "todas_metas_fechar/",
        ListaTodasMetasFechar.as_view(),
        name="todas_metas_fechar",
    ),
    path(
        "form_cadastro_indicador/",
        FormCadastroIndicador.as_view(),
        name="form_cadastro_indicador",
    ),
    path(
        "fechar_form_cadastro_indicador/",
        FecharFormCadastroIndicador.as_view(),
        name="fechar_form_cadastro_indicador",
    ),
    path(
        "form_cadastro_meta/",
        FormCadastroMeta.as_view(),
        name="form_cadastro_meta",
    ),
    path(
        "fechar_form_cadastro_meta/",
        FecharFormCadastroMeta.as_view(),
        name="fechar_form_cadastro_meta",
    ),
]

urlpatterns += htmx_urls
