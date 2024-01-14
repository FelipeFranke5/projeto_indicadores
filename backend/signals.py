from typing import Any
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Indicador, MetaIndicador
from .signals_metas import cadastro_meta_recursivo


@receiver(post_save, sender=Indicador)
def verificar_resultados(
    sender: Indicador, instance: Indicador, created: bool, **kwargs: dict[str, Any]
) -> None:
    if created:
        cadastro_meta_recursivo(instance)


@receiver(post_save, sender=MetaIndicador)
def atualizar_indicadores(
    sender: MetaIndicador, instance: MetaIndicador, **kwargs: dict[str, Any]
) -> None:
    indicadores = Indicador.objects.all()
    metas = MetaIndicador.objects.all()

    if indicadores.exists():
        if len(metas) > 1:
            for indicador in indicadores:
                indicador.meta_desatualizada = True
                indicador.save(force_update=True)
