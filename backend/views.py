from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Indicador, MetaIndicador
from .serializers import IndicadorSerializer, MetaIndicadorSerializer
from .autenticacao import AutenticacaoUsuario


@api_view(["GET"])
def lista_todos_indicadores(request: Request, id_usuario: int) -> Response:
    autenticacao = AutenticacaoUsuario(request)
    retorno_validacao = autenticacao.validar_igualdade_tokens(id_usuario)

    if retorno_validacao is not None:
        return retorno_validacao

    operador = autenticacao.obter_operador(id_usuario)
    indicadores = Indicador.objects.filter(operador=operador).order_by("data_registro")
    serializer = IndicadorSerializer(indicadores, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def lista_metas(request: Request) -> Response:
    metas = MetaIndicador.objects.all().order_by("data_referencia")
    serializer = MetaIndicadorSerializer(metas, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def cadastrar_indicador(request: Request, id_usuario: int) -> Response:
    autenticacao = AutenticacaoUsuario(request)
    retorno_validacao = autenticacao.validar_igualdade_tokens(id_usuario)

    if retorno_validacao is not None:
        return retorno_validacao

    operador = autenticacao.obter_operador(id_usuario)
    serializer = IndicadorSerializer(data=request.data)

    if serializer.is_valid():
        serializer.validated_data["operador"] = operador
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def cadastrar_meta(request: Request) -> Response:
    serializer = MetaIndicadorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def remover_indicador(request: Request, pk: int, id_usuario: int) -> Response:
    autenticacao = AutenticacaoUsuario(request)
    retorno_validacao = autenticacao.validar_igualdade_tokens(id_usuario)

    if retorno_validacao is not None:
        return retorno_validacao

    operador = autenticacao.obter_operador(id_usuario)

    try:
        indicador = Indicador.objects.get(pk=pk, operador=operador)
    except Indicador.DoesNotExist:
        return Response(
            data={"erro": "O indicador não foi encontrado."},
            headers={"WWW-Authenticate": "Token"},
            status=status.HTTP_404_NOT_FOUND,
        )

    indicador.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["DELETE"])
def remover_meta(request: Request, pk: int) -> Response:
    try:
        meta = MetaIndicador.objects.get(pk=pk)
    except MetaIndicador.DoesNotExist:
        return Response(
            data={"erro": "A meta não foi encontrada."},
            status=status.HTTP_404_NOT_FOUND,
        )

    meta.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
