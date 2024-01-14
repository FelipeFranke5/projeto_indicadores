# TODO: Limpar esse código, utilizando classes.

from random import randint
from .models import Indicador, MetaIndicador, IndicadorDentroMeta, IndicadorForaMeta


def cadastro_meta_recursivo(instance: Indicador, metas_exists: bool = False) -> None:
    metas = MetaIndicador.objects.all()

    if metas_exists:
        meta_mais_recente = metas.last()

        if meta_mais_recente:
            contador = 0
            diferenca_tmo = float(instance.tmo - meta_mais_recente.tmo)

            if instance.tmo <= meta_mais_recente.tmo:
                contador += 1
                tmo_dentro = IndicadorDentroMeta.objects.get_or_create(
                    nome_indicador="tmo", diferenca=diferenca_tmo
                )[0]

                instance.indicadores_dentro_meta.add(tmo_dentro)
            else:
                tmo_fora = IndicadorForaMeta.objects.get_or_create(
                    nome_indicador="tmo", diferenca=diferenca_tmo
                )[0]

                instance.indicadores_fora_meta.add(tmo_fora)

            diferenca_aderencia = instance.aderencia - meta_mais_recente.aderencia

            if instance.aderencia >= meta_mais_recente.aderencia:
                contador += 1
                aderencia_dentro = IndicadorDentroMeta.objects.get_or_create(
                    nome_indicador="aderencia", diferenca=diferenca_aderencia
                )[0]

                instance.indicadores_dentro_meta.add(aderencia_dentro)
            else:
                aderencia_fora = IndicadorForaMeta.objects.get_or_create(
                    nome_indicador="aderencia", diferenca=diferenca_aderencia
                )[0]

                instance.indicadores_fora_meta.add(aderencia_fora)

            diferenca_nps2 = instance.nps2 - meta_mais_recente.nps2

            if instance.nps2 >= meta_mais_recente.nps2:
                contador += 1
                nps2_dentro = IndicadorDentroMeta.objects.get_or_create(
                    nome_indicador="nps2", diferenca=diferenca_nps2
                )[0]

                instance.indicadores_dentro_meta.add(nps2_dentro)
            else:
                nps2_fora = IndicadorForaMeta.objects.get_or_create(
                    nome_indicador="nps2", diferenca=diferenca_nps2
                )[0]

                instance.indicadores_fora_meta.add(nps2_fora)

            diferenca_nps3 = instance.nps3 - meta_mais_recente.nps3

            if instance.nps3 >= meta_mais_recente.nps3:
                contador += 1
                nps3_dentro = IndicadorDentroMeta.objects.get_or_create(
                    nome_indicador="nps3", diferenca=diferenca_nps3
                )[0]

                instance.indicadores_dentro_meta.add(nps3_dentro)
            else:
                nps3_fora = IndicadorForaMeta.objects.get_or_create(
                    nome_indicador="nps3", diferenca=diferenca_nps3
                )[0]

                instance.indicadores_fora_meta.add(nps3_fora)

            diferenca_rechamada = instance.rechamada - meta_mais_recente.rechamada

            if instance.rechamada <= meta_mais_recente.rechamada:
                contador += 1
                rechamada_dentro = IndicadorDentroMeta.objects.get_or_create(
                    nome_indicador="rechamada", diferenca=diferenca_rechamada
                )[0]

                instance.indicadores_dentro_meta.add(rechamada_dentro)
            else:
                rechamada_fora = IndicadorForaMeta.objects.get_or_create(
                    nome_indicador="rechamada", diferenca=diferenca_rechamada
                )[0]

                instance.indicadores_fora_meta.add(rechamada_fora)

            diferenca_shortcall = instance.shortcall - meta_mais_recente.shortcall

            if instance.shortcall <= meta_mais_recente.shortcall:
                contador += 1
                shortcall_dentro = IndicadorDentroMeta.objects.get_or_create(
                    nome_indicador="shortcall", diferenca=diferenca_shortcall
                )[0]

                instance.indicadores_dentro_meta.add(shortcall_dentro)
            else:
                shortcall_fora = IndicadorForaMeta.objects.get_or_create(
                    nome_indicador="shortcall", diferenca=diferenca_shortcall
                )[0]

                instance.indicadores_fora_meta.add(shortcall_fora)

            diferenca_abs = instance.abs - meta_mais_recente.abs

            if instance.abs <= meta_mais_recente.abs:
                contador += 1
                abs_dentro = IndicadorDentroMeta.objects.get_or_create(
                    nome_indicador="abs", diferenca=diferenca_abs
                )[0]

                instance.indicadores_dentro_meta.add(abs_dentro)
            else:
                abs_fora = IndicadorForaMeta.objects.get_or_create(
                    nome_indicador="abs", diferenca=diferenca_abs
                )[0]

                instance.indicadores_fora_meta.add(abs_fora)

            diferenca_transf_demais_ilhas = (
                instance.transf_demais_ilhas - meta_mais_recente.transf_demais_ilhas
            )

            if instance.transf_demais_ilhas >= meta_mais_recente.transf_demais_ilhas:
                contador += 1
                transf_demais_ilhas_dentro = IndicadorDentroMeta.objects.get_or_create(
                    nome_indicador="transf_demais_ilhas",
                    diferenca=diferenca_transf_demais_ilhas,
                )[0]

                instance.indicadores_dentro_meta.add(transf_demais_ilhas_dentro)
            else:
                transf_demais_ilhas_fora = IndicadorForaMeta.objects.get_or_create(
                    nome_indicador="transf_demais_ilhas",
                    diferenca=diferenca_transf_demais_ilhas,
                )[0]

                instance.indicadores_fora_meta.add(transf_demais_ilhas_fora)

            diferenca_transf_pesquisa = (
                instance.transf_pesquisa - meta_mais_recente.transf_pesquisa
            )

            if instance.transf_pesquisa >= meta_mais_recente.transf_pesquisa:
                contador += 1
                transf_pesquisa_dentro = IndicadorDentroMeta.objects.get_or_create(
                    nome_indicador="transf_pesquisa",
                    diferenca=diferenca_transf_pesquisa,
                )[0]

                instance.indicadores_dentro_meta.add(transf_pesquisa_dentro)
            else:
                transf_pesquisa_fora = IndicadorForaMeta.objects.get_or_create(
                    nome_indicador="transf_pesquisa",
                    diferenca=diferenca_transf_pesquisa,
                )[0]

                instance.indicadores_fora_meta.add(transf_pesquisa_fora)

            if contador == 9:
                instance.dentro_meta = True
            else:
                instance.dentro_meta = False
            return
        return

    if not metas.exists():
        MetaIndicador.objects.create(
            tmo=randint(100, 600),
            aderencia=randint(80, 100),
            nps2=randint(75, 100),
            nps3=randint(75, 100),
            rechamada=randint(10, 20),
            shortcall=randint(10, 20),
            abs=randint(3, 10),
            transf_demais_ilhas=randint(80, 100),
            transf_pesquisa=randint(80, 100),
        )
        cadastro_meta_recursivo(instance, metas_exists=True)
    else:
        cadastro_meta_recursivo(instance, metas_exists=True)
