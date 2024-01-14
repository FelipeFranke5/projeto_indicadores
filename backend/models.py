from django.db import models
from django.contrib.auth.models import User


class IndicadorDentroMeta(models.Model):
    nome_indicador = models.CharField(max_length=100)
    diferenca = models.FloatField()


class IndicadorForaMeta(models.Model):
    nome_indicador = models.CharField(max_length=100)
    diferenca = models.FloatField()


class Indicador(models.Model):
    operador = models.ForeignKey(User, on_delete=models.CASCADE)
    data_registro = models.DateField(auto_now_add=True)
    tmo = models.IntegerField()
    aderencia = models.FloatField()
    nps2 = models.FloatField()
    nps3 = models.FloatField()
    rechamada = models.FloatField()
    shortcall = models.FloatField()
    abs = models.FloatField()
    transf_demais_ilhas = models.FloatField()
    transf_pesquisa = models.FloatField()
    dentro_meta = models.BooleanField(null=True, blank=True, default=False)
    indicadores_dentro_meta = models.ManyToManyField(
        IndicadorDentroMeta,
        blank=True,
        related_name="indicadores_dentro",
    )
    indicadores_fora_meta = models.ManyToManyField(
        IndicadorForaMeta,
        blank=True,
        related_name="indicadores_fora",
    )
    meta_desatualizada = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        verbose_name = "indicador"
        verbose_name_plural = "indicadores"

    def __str__(self):
        return self.operador.username


class MetaIndicador(models.Model):
    data_referencia = models.DateField(auto_now_add=True)
    tmo = models.IntegerField()
    aderencia = models.FloatField()
    nps2 = models.FloatField()
    nps3 = models.FloatField()
    rechamada = models.FloatField()
    shortcall = models.FloatField()
    abs = models.FloatField()
    transf_demais_ilhas = models.FloatField()
    transf_pesquisa = models.FloatField()

    class Meta:
        verbose_name = "metaindicador"
        verbose_name_plural = "metaindicadores"

    def __str__(self):
        return f"Meta de indicador - {self.data_referencia}"
