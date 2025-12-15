"""
Sistema de Cadastro de Usuários
Arquivo executável para teste manual do cadastro.
Mantém histórico local em arquivo JSON.
"""

import sys
import os
import json

# Adiciona a pasta src ao path para permitir imports
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
)

from validators import validar_email, validar_senha


ARQUIVO_DADOS = "dados_usuarios.json"


class Usuario:
    """Representa um usuário do sistema."""

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def to_dict(self):
        return {
            "email": self.email,
            "senha": self.senha
        }

    @staticmethod
    def from_dict(dados):
        return Usuario(dados["email"], dados["senha"])


class SistemaCadastro:
    """Sistema de cadastro com persistência local."""

    def __init__(self):
        self.usuarios = []
        self._carregar_dados()

    def _carregar_dados(self):
        """Carrega usuários do arquivo JSON, se existir."""
        if os.path.exists(ARQUIVO_DADOS):
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                for item in dados:
                    self.usuarios.append(Usuario.from_dict(item))

    def _salvar_dados(self):
        """Salva usuários no arquivo JSON."""
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(
                [u.to_dict() for u in self.usuarios],
                arquivo,
                indent=4,
                ensure_ascii=False
            )

    def cadastrar_usuario(self, email, senha):
        """Cadastra um novo usuário com validações."""

        if not validar_email(email):
            return False, "E-mail inválido. Formato correto: exemplo@dominio.com"

        if not validar_senha(senha):
            return False, "Senha inválida. Deve ter ao menos 6 caracteres e 1 número."

        if self.buscar_usuario(email) is not None:
            return False, "E-mail já cadastrado no sistema."

        novo_usuario = Usuario(email, senha)
        self.usuarios.append(novo_usuario)
        self._salvar_dados()

        return True, "Usuário cadastrado com sucesso!"

    def buscar_usuario(self, email):
        """Busca usuário pelo e-mail."""
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None

    def obter_historico(self):
        """Retorna histórico de usuários."""
        return self.usuarios.copy()

    def contar_usuarios(self):
        """Retorna total de usuários cadastrados."""
        return len(self.usuarios)


# ==========================
# EXECUÇÃO MANUAL DO SISTEMA
# ==========================
if __name__ == "__main__":
    sistema = SistemaCadastro()

    print("=" * 50)
    print("TESTE MANUAL - SISTEMA DE CADASTRO")
    print("=" * 50)

    print("\n1️⃣ Cadastro válido:")
    print(sistema.cadastrar_usuario("teste@teste.com", "senha123"))

    print("\n2️⃣ Cadastro duplicado:")
    print(sistema.cadastrar_usuario("teste@teste.com", "outrasenha1"))

    print("\n3️⃣ Cadastro com e-mail inválido:")
    print(sistema.cadastrar_usuario("email_invalido", "senha123"))

    print("\n4️⃣ Cadastro com senha inválida:")
    print(sistema.cadastrar_usuario("novo@teste.com", "abc12"))

    print("\n5️⃣ Busca usuário existente:")
    usuario = sistema.buscar_usuario("teste@teste.com")
    print(usuario.email if usuario else "Não encontrado")

    print("\n6️⃣ Histórico completo:")
    for i, u in enumerate(sistema.obter_historico(), 1):
        print(f"{i}. {u.email}")

    print("\nTotal de usuários cadastrados:", sistema.contar_usuarios())
    print("=" * 50)
