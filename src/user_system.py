"""
Sistema de Cadastro de Usuários.
Permite cadastrar, buscar e manter histórico de usuários com validações.
"""

from validators import validar_email, validar_senha


class Usuario:
    """Classe que representa um usuário do sistema."""
    
    def __init__(self, email, senha):
        """
        Inicializa um novo usuário.
        
        Args:
            email (str): E-mail do usuário
            senha (str): Senha do usuário
        """
        self.email = email
        self.senha = senha


class SistemaCadastro:
    """
    Sistema de cadastro e gerenciamento de usuários.
    Mantém histórico de todos os usuários cadastrados.
    """
    
    def __init__(self):
        """Inicializa o sistema com uma lista vazia de usuários."""
        self.usuarios = []  # Histórico de usuários cadastrados
    
    def cadastrar_usuario(self, email, senha):
        """
        Cadastra um novo usuário no sistema (RF01).
        Valida e-mail (RF02) e senha (RF03) antes de cadastrar.
        
        Args:
            email (str): E-mail do usuário
            senha (str): Senha do usuário
            
        Returns:
            tuple: (bool, str) - (sucesso, mensagem)
        """
        # Validação de e-mail (RF02)
        if not validar_email(email):
            return False, "E-mail inválido. Formato correto: exemplo@dominio.com"
        
        # Validação de senha (RF03)
        if not validar_senha(senha):
            return False, "Senha inválida. Deve ter ao menos 6 caracteres e 1 número."
        
        # Verifica se o e-mail já está cadastrado
        if self.buscar_usuario(email) is not None:
            return False, "E-mail já cadastrado no sistema."
        
        # Cria e adiciona o usuário ao histórico (RF05)
        novo_usuario = Usuario(email, senha)
        self.usuarios.append(novo_usuario)
        
        return True, "Usuário cadastrado com sucesso!"
    
    def buscar_usuario(self, email):
        """
        Busca um usuário pelo e-mail (RF04).
        
        Args:
            email (str): E-mail do usuário a ser buscado
            
        Returns:
            Usuario ou None: Usuário encontrado ou None se não encontrado
        """
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None
    
    def obter_historico(self):
        """
        Retorna o histórico completo de usuários cadastrados (RF05).
        
        Returns:
            list: Lista de todos os usuários cadastrados
        """
        return self.usuarios.copy()
    
    def contar_usuarios(self):
        """
        Retorna a quantidade de usuários cadastrados.
        
        Returns:
            int: Número de usuários no sistema
        """
        return len(self.usuarios)

