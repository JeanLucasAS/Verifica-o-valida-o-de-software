"""
Módulo de validações para o sistema de cadastro de usuários.
Contém funções para validar e-mail e senha.
"""

import re


def validar_email(email):
    """
    Valida se o e-mail fornecido é válido.
    
    Args:
        email (str): E-mail a ser validado
        
    Returns:
        bool: True se o e-mail é válido, False caso contrário
    """
    # Padrão básico de validação de e-mail
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))


def validar_senha(senha):
    """
    Valida se a senha possui ao menos 6 caracteres e 1 número.
    
    Args:
        senha (str): Senha a ser validada
        
    Returns:
        bool: True se a senha é válida, False caso contrário
    """
    # Verifica se tem pelo menos 6 caracteres
    if len(senha) < 6:
        return False
    
    # Verifica se contém pelo menos 1 número
    if not any(char.isdigit() for char in senha):
        return False
    
    return True

