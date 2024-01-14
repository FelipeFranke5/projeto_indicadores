import re
from django.http import HttpRequest


class ValidacaoNomeUsuario:
    def __init__(self, request: HttpRequest) -> None:
        self.request = request
        self.usuario = None

    def obter_usuario(self) -> str | None:
        self.usuario = self.request.POST.get("username")
        return self.usuario

    def usuario_esta_vazio(self) -> bool:
        usuario = self.obter_usuario()
        campo = r"^$"
        padrao = re.compile(campo)
        regex = re.fullmatch(pattern=padrao, string=usuario)
        return regex is not None

    def usuario_excede_caracteres(self) -> bool:
        usuario = self.obter_usuario()
        return len(usuario) > 150

    def usuario_nao_tem_minimo_recomendado(self) -> bool:
        usuario = self.obter_usuario()
        return len(usuario) < 5

    def usuario_possui_caracteres_nao_permitidos(self) -> bool:
        usuario = self.obter_usuario()
        campo = r"[\!#\$%¨&*\(\)]"
        padrao = re.compile(campo)
        regex = re.findall(pattern=padrao, string=usuario)
        return len(regex) != 0

    def usuario_possui_caracteres_permitidos(self) -> bool:
        usuario = self.obter_usuario()
        campo = r"[@/\.\+-_]"
        padrao = re.compile(pattern=campo)
        regex = re.findall(pattern=padrao, string=usuario)
        return len(regex) != 0

    def usuario_alfanumerico(self) -> bool:
        usuario = self.obter_usuario()
        campo = r"[\w]+"
        padrao = re.compile(campo)
        regex = re.findall(pattern=padrao, string=usuario)
        return len(regex) != 0


class ValidacaoSenha1:
    def __init__(self, request: HttpRequest) -> None:
        self.request = request
        self.senha1 = None
        self.usuario = None

    def obter_senha1(self) -> str | None:
        self.senha1 = self.request.POST.get("password1")
        return self.senha1

    def obter_usuario(self) -> str | None:
        self.usuario = self.request.POST.get("username")
        return self.usuario

    def senha1_esta_vazia(self) -> bool:
        senha1 = self.obter_senha1()
        campo = r"^$"
        padrao = re.compile(campo)
        regex = re.fullmatch(pattern=padrao, string=senha1)
        return regex is not None

    def senha1_excede_caracteres(self) -> bool:
        senha1 = self.obter_senha1()
        return len(senha1) > 128

    def senha1_semelhante_usuario(self) -> bool:
        usuario = self.obter_usuario()
        senha1 = self.obter_senha1()

        if not usuario or not senha1:
            return False
        if usuario.lower().strip() == senha1.lower().strip():
            return True

        similares: list[str] = []
        for letra_usuario in usuario.lower().strip():
            for letra_senha1 in senha1.lower().strip():
                if letra_senha1 == letra_usuario:
                    similares.append(letra_senha1)
        return len(similares) >= 5


class ValidacaoSenha2:
    def __init__(self, request: HttpRequest) -> None:
        self.request = request
        self.senha1 = None
        self.senha2 = None

    def obter_senha1(self) -> str | None:
        self.senha1 = self.request.POST.get("password1")
        return self.senha1

    def obter_senha2(self) -> str | None:
        self.senha2 = self.request.POST.get("password2")
        return self.senha2

    def senha2_esta_vazia(self) -> bool:
        senha2 = self.obter_senha2()
        campo = r"^$"
        padrao = re.compile(campo)
        regex = re.fullmatch(pattern=padrao, string=senha2)
        return regex is not None

    def senha2_igual_senha1(self) -> bool:
        senha1 = self.obter_senha1()
        senha2 = self.obter_senha2()

        if not senha1 or not senha2:
            return False
        return senha1.lower().strip() == senha2.lower().strip()
