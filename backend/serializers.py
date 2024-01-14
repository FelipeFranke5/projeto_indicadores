from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Indicador, MetaIndicador


class IndicadorSerializer(serializers.ModelSerializer):
    data_registro = serializers.DateField(format="%d-%m-%Y", read_only=True)  # type: ignore

    indicadores_dentro_meta = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="nome_indicador"
    )

    indicadores_fora_meta = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="nome_indicador"
    )

    class Meta:
        model = Indicador
        exclude = ["operador"]


class MetaIndicadorSerializer(serializers.ModelSerializer):
    data_referencia = serializers.DateField(format="%d-%m-%Y", read_only=True)  # type: ignore

    class Meta:
        model = MetaIndicador
        fields = "__all__"
