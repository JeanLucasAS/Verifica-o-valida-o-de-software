"""
Testes automatizados para o sistema de cadastro de usuários.
Utiliza unittest para validar todos os requisitos funcionais.
"""

import unittest
import sys
import os

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.user_system import SistemaCadastro
from src.validators import validar_email, validar_senha


class TestValidadores(unittest.TestCase):
    """Testes para as funções de validação."""
    
    def test_validar_email_valido(self):
        """
        Teste CT01: Validação de e-mail válido.
        Objetivo: Verificar se e-mails válidos são aceitos.
        """
        # E-mails válidos
        self.assertTrue(validar_email("usuario@exemplo.com"))
        self.assertTrue(validar_email("teste123@dominio.com.br"))
        self.assertTrue(validar_email("nome.sobrenome@empresa.co.uk"))
    
    def test_validar_email_invalido(self):
        """
        Teste CT02: Validação de e-mail inválido.
        Objetivo: Verificar se e-mails inválidos são rejeitados.
        """
        # E-mails inválidos
        self.assertFalse(validar_email("email_sem_arroba.com"))
        self.assertFalse(validar_email("@sem_usuario.com"))
        self.assertFalse(validar_email("usuario@sem_dominio"))
        self.assertFalse(validar_email(""))
    
    def test_validar_senha_valida(self):
        """
        Teste CT03: Validação de senha válida.
        Objetivo: Verificar se senhas com 6+ caracteres e 1+ número são aceitas.
        """
        # Senhas válidas
        self.assertTrue(validar_senha("senha123"))
        self.assertTrue(validar_senha("abc123"))
        self.assertTrue(validar_senha("minhasenha9"))
    
    def test_validar_senha_invalida(self):
        """
        Teste CT04: Validação de senha inválida.
        Objetivo: Verificar se senhas sem número ou com menos de 6 caracteres são rejeitadas.
        """
        # Senha muito curta
        self.assertFalse(validar_senha("abc12"))  # Menos de 6 caracteres
        
        # Senha sem número
        self.assertFalse(validar_senha("senhasemnumero"))
        
        # Senha vazia
        self.assertFalse(validar_senha(""))


class TestSistemaCadastro(unittest.TestCase):
    """Testes para o sistema de cadastro de usuários."""
    
    def setUp(self):
        """
        Configuração inicial para cada teste.
        Cria uma nova instância do sistema antes de cada teste.
        """
        self.sistema = SistemaCadastro()
    
    def test_cadastrar_usuario_valido(self):
        """
        Teste CT05: Cadastro de usuário válido.
        Objetivo: Verificar se usuários com e-mail e senha válidos são cadastrados.
        Entrada: email="teste@exemplo.com", senha="senha123"
        Resultado Esperado: Cadastro bem-sucedido
        """
        sucesso, mensagem = self.sistema.cadastrar_usuario("teste@exemplo.com", "senha123")
        
        # Verifica se o cadastro foi bem-sucedido
        self.assertTrue(sucesso)
        self.assertEqual(mensagem, "Usuário cadastrado com sucesso!")
        
        # Verifica se o usuário foi adicionado ao histórico
        self.assertEqual(self.sistema.contar_usuarios(), 1)
    
    def test_cadastrar_usuario_email_invalido(self):
        """
        Teste CT06: Cadastro com e-mail inválido.
        Objetivo: Verificar se o sistema rejeita cadastros com e-mail inválido (RF02).
        Entrada: email="email_invalido", senha="senha123"
        Resultado Esperado: Cadastro rejeitado com mensagem de erro
        """
        sucesso, mensagem = self.sistema.cadastrar_usuario("email_invalido", "senha123")
        
        # Verifica se o cadastro foi rejeitado
        self.assertFalse(sucesso)
        self.assertIn("E-mail inválido", mensagem)
        
        # Verifica que nenhum usuário foi cadastrado
        self.assertEqual(self.sistema.contar_usuarios(), 0)
    
    def test_cadastrar_usuario_senha_invalida(self):
        """
        Teste CT07: Cadastro com senha inválida.
        Objetivo: Verificar se o sistema rejeita cadastros com senha inválida (RF03).
        Entrada: email="teste@exemplo.com", senha="abc12" (menos de 6 caracteres)
        Resultado Esperado: Cadastro rejeitado com mensagem de erro
        """
        sucesso, mensagem = self.sistema.cadastrar_usuario("teste@exemplo.com", "abc12")
        
        # Verifica se o cadastro foi rejeitado
        self.assertFalse(sucesso)
        self.assertIn("Senha inválida", mensagem)
        
        # Verifica que nenhum usuário foi cadastrado
        self.assertEqual(self.sistema.contar_usuarios(), 0)
    
    def test_buscar_usuario_existente(self):
        """
        Teste CT08: Buscar usuário existente.
        Objetivo: Verificar se a busca por e-mail retorna o usuário correto (RF04).
        Entrada: email="usuario@teste.com"
        Resultado Esperado: Usuário encontrado
        """
        # Primeiro cadastra um usuário
        self.sistema.cadastrar_usuario("usuario@teste.com", "senha123")
        
        # Busca o usuário
        usuario_encontrado = self.sistema.buscar_usuario("usuario@teste.com")
        
        # Verifica se o usuário foi encontrado
        self.assertIsNotNone(usuario_encontrado)
        self.assertEqual(usuario_encontrado.email, "usuario@teste.com")
    
    def test_buscar_usuario_inexistente(self):
        """
        Teste CT09: Buscar usuário inexistente.
        Objetivo: Verificar se a busca por e-mail inexistente retorna None (RF04).
        Entrada: email="naoexiste@teste.com"
        Resultado Esperado: None (usuário não encontrado)
        """
        # Busca um usuário que não existe
        usuario_encontrado = self.sistema.buscar_usuario("naoexiste@teste.com")
        
        # Verifica que nenhum usuário foi encontrado
        self.assertIsNone(usuario_encontrado)
    
    def test_manter_historico_usuarios(self):
        """
        Teste CT10: Manter histórico de usuários.
        Objetivo: Verificar se o sistema mantém histórico de todos os usuários cadastrados (RF05).
        Entrada: Cadastro de 3 usuários válidos
        Resultado Esperado: Histórico contém os 3 usuários
        """
        # Cadastra múltiplos usuários
        self.sistema.cadastrar_usuario("user1@teste.com", "senha123")
        self.sistema.cadastrar_usuario("user2@teste.com", "senha456")
        self.sistema.cadastrar_usuario("user3@teste.com", "senha789")
        
        # Obtém o histórico
        historico = self.sistema.obter_historico()
        
        # Verifica se o histórico contém todos os usuários
        self.assertEqual(len(historico), 3)
        
        # Verifica se os e-mails estão corretos
        emails = [usuario.email for usuario in historico]
        self.assertIn("user1@teste.com", emails)
        self.assertIn("user2@teste.com", emails)
        self.assertIn("user3@teste.com", emails)
    
    def test_cadastrar_email_duplicado(self):
        """
        Teste adicional: Prevenir cadastro de e-mail duplicado.
        Objetivo: Verificar se o sistema impede cadastro de e-mail já existente.
        """
        # Cadastra o primeiro usuário
        self.sistema.cadastrar_usuario("duplicado@teste.com", "senha123")
        
        # Tenta cadastrar o mesmo e-mail novamente
        sucesso, mensagem = self.sistema.cadastrar_usuario("duplicado@teste.com", "outrasenha456")
        
        # Verifica se o cadastro foi rejeitado
        self.assertFalse(sucesso)
        self.assertIn("já cadastrado", mensagem)
        
        # Verifica que apenas um usuário foi cadastrado
        self.assertEqual(self.sistema.contar_usuarios(), 1)


if __name__ == '__main__':
    # Executa todos os testes
    unittest.main(verbosity=2)

