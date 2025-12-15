# Plano de Testes Funcionais - Sistema de Cadastro de Usuários

## Requisitos Testados

### Requisitos Funcionais (RF)
- **RF01**: O sistema deve permitir o cadastro de um novo usuário.
- **RF02**: O sistema deve validar se o e-mail fornecido é válido no momento do cadastro.
- **RF03**: O sistema deve validar se a senha possui ao menos 6 caracteres e 1 número.
- **RF04**: O sistema deve permitir buscar um usuário pelo e-mail.
- **RF05**: O sistema deve manter um histórico dos usuários cadastrados.

---

## Casos de Teste

### CT01 - Validação de E-mail Válido
- **Identificador**: CT01
- **Requisito Testado**: RF02
- **Objetivo do Teste**: Verificar se e-mails válidos são aceitos pelo sistema de validação.
- **Entrada**: 
  - "usuario@exemplo.com"
  - "teste123@dominio.com.br"
  - "nome.sobrenome@empresa.co.uk"
- **Resultado Esperado**: Todas as validações retornam `True` (e-mail válido).
- **Resultado Obtido**: ✅ Todas as validações retornaram `True`.
- **Status**: ✅ **Aprovado**

---

### CT02 - Validação de E-mail Inválido
- **Identificador**: CT02
- **Requisito Testado**: RF02
- **Objetivo do Teste**: Verificar se e-mails inválidos são rejeitados pelo sistema de validação.
- **Entrada**: 
  - "email_sem_arroba.com"
  - "@sem_usuario.com"
  - "usuario@sem_dominio"
  - "" (string vazia)
- **Resultado Esperado**: Todas as validações retornam `False` (e-mail inválido).
- **Resultado Obtido**: ✅ Todas as validações retornaram `False`.
- **Status**: ✅ **Aprovado**

---

### CT03 - Validação de Senha Válida
- **Identificador**: CT03
- **Requisito Testado**: RF03
- **Objetivo do Teste**: Verificar se senhas com 6 ou mais caracteres e pelo menos 1 número são aceitas.
- **Entrada**: 
  - "senha123"
  - "abc123"
  - "minhasenha9"
- **Resultado Esperado**: Todas as validações retornam `True` (senha válida).
- **Resultado Obtido**: ✅ Todas as validações retornaram `True`.
- **Status**: ✅ **Aprovado**

---

### CT04 - Validação de Senha Inválida
- **Identificador**: CT04
- **Requisito Testado**: RF03
- **Objetivo do Teste**: Verificar se senhas sem número ou com menos de 6 caracteres são rejeitadas.
- **Entrada**: 
  - "abc12" (menos de 6 caracteres)
  - "senhasemnumero" (sem número)
  - "" (string vazia)
- **Resultado Esperado**: Todas as validações retornam `False` (senha inválida).
- **Resultado Obtido**: ✅ Todas as validações retornaram `False`.
- **Status**: ✅ **Aprovado**

---

### CT05 - Cadastro de Usuário Válido
- **Identificador**: CT05
- **Requisito Testado**: RF01, RF02, RF03, RF05
- **Objetivo do Teste**: Verificar se usuários com e-mail e senha válidos são cadastrados com sucesso e adicionados ao histórico.
- **Entrada**: 
  - email: "teste@exemplo.com"
  - senha: "senha123"
- **Resultado Esperado**: 
  - Cadastro bem-sucedido (retorna `True`)
  - Mensagem: "Usuário cadastrado com sucesso!"
  - Usuário adicionado ao histórico
- **Resultado Obtido**: ✅ Cadastro realizado com sucesso. Usuário adicionado ao histórico.
- **Status**: ✅ **Aprovado**

---

### CT06 - Cadastro com E-mail Inválido
- **Identificador**: CT06
- **Requisito Testado**: RF01, RF02
- **Objetivo do Teste**: Verificar se o sistema rejeita cadastros com e-mail inválido.
- **Entrada**: 
  - email: "email_invalido"
  - senha: "senha123"
- **Resultado Esperado**: 
  - Cadastro rejeitado (retorna `False`)
  - Mensagem contendo "E-mail inválido"
  - Nenhum usuário cadastrado
- **Resultado Obtido**: ✅ Cadastro rejeitado corretamente. Mensagem de erro exibida.
- **Status**: ✅ **Aprovado**

---

### CT07 - Cadastro com Senha Inválida
- **Identificador**: CT07
- **Requisito Testado**: RF01, RF03
- **Objetivo do Teste**: Verificar se o sistema rejeita cadastros com senha inválida.
- **Entrada**: 
  - email: "teste@exemplo.com"
  - senha: "abc12" (menos de 6 caracteres)
- **Resultado Esperado**: 
  - Cadastro rejeitado (retorna `False`)
  - Mensagem contendo "Senha inválida"
  - Nenhum usuário cadastrado
- **Resultado Obtido**: ✅ Cadastro rejeitado corretamente. Mensagem de erro exibida.
- **Status**: ✅ **Aprovado**

---

### CT08 - Buscar Usuário Existente
- **Identificador**: CT08
- **Requisito Testado**: RF04
- **Objetivo do Teste**: Verificar se a busca por e-mail retorna o usuário correto quando ele existe no sistema.
- **Entrada**: 
  - email: "usuario@teste.com" (após cadastrar este usuário)
- **Resultado Esperado**: 
  - Usuário encontrado (retorna objeto `Usuario`)
  - E-mail do usuário encontrado corresponde ao buscado
- **Resultado Obtido**: ✅ Usuário encontrado corretamente.
- **Status**: ✅ **Aprovado**

---

### CT09 - Buscar Usuário Inexistente
- **Identificador**: CT09
- **Requisito Testado**: RF04
- **Objetivo do Teste**: Verificar se a busca por e-mail inexistente retorna `None`.
- **Entrada**: 
  - email: "naoexiste@teste.com"
- **Resultado Esperado**: 
  - Retorna `None` (usuário não encontrado)
- **Resultado Obtido**: ✅ Retornou `None` corretamente.
- **Status**: ✅ **Aprovado**

---

### CT10 - Manter Histórico de Usuários
- **Identificador**: CT10
- **Requisito Testado**: RF05
- **Objetivo do Teste**: Verificar se o sistema mantém histórico de todos os usuários cadastrados.
- **Entrada**: 
  - Cadastro de 3 usuários válidos:
    - "user1@teste.com" / "senha123"
    - "user2@teste.com" / "senha456"
    - "user3@teste.com" / "senha789"
- **Resultado Esperado**: 
  - Histórico contém exatamente 3 usuários
  - Todos os e-mails cadastrados estão presentes no histórico
- **Resultado Obtido**: ✅ Histórico mantido corretamente com todos os 3 usuários.
- **Status**: ✅ **Aprovado**

---

## Resumo dos Testes

| CT | Requisito | Status |
|----|-----------|--------|
| CT01 | RF02 | ✅ Aprovado |
| CT02 | RF02 | ✅ Aprovado |
| CT03 | RF03 | ✅ Aprovado |
| CT04 | RF03 | ✅ Aprovado |
| CT05 | RF01, RF02, RF03, RF05 | ✅ Aprovado |
| CT06 | RF01, RF02 | ✅ Aprovado |
| CT07 | RF01, RF03 | ✅ Aprovado |
| CT08 | RF04 | ✅ Aprovado |
| CT09 | RF04 | ✅ Aprovado |
| CT10 | RF05 | ✅ Aprovado |

**Total de Testes**: 10 casos de teste
**Testes Aprovados**: 10
**Testes Reprovados**: 0
**Taxa de Aprovação**: 100%

