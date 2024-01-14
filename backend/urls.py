from django.urls import path
from . import views


urlpatterns = [
    path(
        "indicadores/todos/<int:id_usuario>/",
        views.lista_todos_indicadores,
        name="todos",
    ),
    path(
        "indicadores/cadastrar/<int:id_usuario>/",
        views.cadastrar_indicador,
        name="cadastrar",
    ),
    path("indicadores/remover/<int:pk>/", views.remover_indicador, name="remover"),
    path("metas/todos/", views.lista_metas, name="todos"),
    path("metas/cadastrar/", views.cadastrar_meta, name="cadastrar"),
    path(
        "metas/remover/<int:pk>/<int:id_usuario>/", views.remover_meta, name="remover"
    ),
]
