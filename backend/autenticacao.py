from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class AutenticacaoUsuario:
    def __init__(self, request: Request) -> None:
        self.request = request
        self.request_header = None
        self.operador = None
        self.token_operador = None

    def obter_request_header(self) -> Response | str:
        self.request_header: str | None = self.request.META.get("HTTP_AUTHORIZATION")

        if not self.request_header:
            return Response(
                data={"erro:": "Token de Autorização é obrigatório."},
                headers={"WWW-Authenticate": "Token"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return self.request_header

    def obter_token_do_header(self) -> Response | str:
        header = self.obter_request_header()

        if isinstance(header, Response):
            return header
        return header.split()[1]

    def obter_operador(self, id_operador: int) -> Response | User:
        if not isinstance(id_operador, int):
            return Response(
                data={"erro": "ID do Usuário deve ser numérico."},
                headers={"WWW-Authenticate": "Token"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            self.operador = User.objects.get(pk=id_operador)
        except User.DoesNotExist:
            return Response(
                data={"erro": "Usuário não encontrado."},
                headers={"WWW-Authenticate": "Token"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return self.operador

    def obter_token_do_operador(self, operador: Response | User) -> Response | str:
        if not isinstance(operador, User):
            return Response(
                data={
                    "erro": "Argumento fornecido para operador não corresponde à uma instância de User."
                },
                headers={"WWW-Authenticate": "Token"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            self.token_operador = Token.objects.get(user=operador)
        except Token.DoesNotExist:
            return Response(
                data={"erro": "Token não encontrado para este usuário."},
                headers={"WWW-Authenticate": "Token"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return self.token_operador.key

    def validar_igualdade_tokens(self, id_operador: int) -> Response | None:
        operador = self.obter_operador(id_operador)
        token_header = self.obter_token_do_header()
        token_operador = self.obter_token_do_operador(operador)

        if isinstance(operador, Response):
            return operador
        if isinstance(token_header, Response):
            return token_header
        if isinstance(token_operador, Response):
            return token_operador

        if token_header.lower().strip() != token_operador.lower().strip():
            return Response(
                data={"erro": "A autenticação falhou."},
                headers={"WWW-Authenticate": "Token"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return None
