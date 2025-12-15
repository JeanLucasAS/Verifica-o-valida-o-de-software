# Sistema de Cadastro de Usuários

Sistema desenvolvido para a atividade de Verificação e Validação de Software.

## Estrutura do Projeto

```
verificacao e validacao/
├── src/
│   ├── user_system.py      # Sistema principal de cadastro
│   └── validators.py       # Funções de validação (e-mail e senha)
├── tests/
│   └── test_user_system.py # Testes automatizados
├── plano_testes.md         # Plano de testes funcionais
├── requirements.txt        # Dependências do projeto
├── dados_usuarios.json     # Dados dos usuários
└── README.md               # Este arquivo
```

## Requisitos do Sistema

### Requisitos Funcionais (RF)
- **RF01**: O sistema deve permitir o cadastro de um novo usuário.
- **RF02**: O sistema deve validar se o e-mail fornecido é válido no momento do cadastro.
- **RF03**: O sistema deve validar se a senha possui ao menos 6 caracteres e 1 número.
- **RF04**: O sistema deve permitir buscar um usuário pelo e-mail.
- **RF05**: O sistema deve manter um histórico dos usuários cadastrados.

### Requisitos Não Funcionais (RNF)
- **RNF01**: O sistema deve ser implementado na linguagem Python.
- **RNF02**: O código deve ser modularizado, com separação entre lógica e testes.

## Como Executar

### Pré-requisitos
- Python 3.7 ou superior instalado
- (Opcional) `reportlab` para gerar PDF: `pip install reportlab`

### Passo a Passo Rápido

#### 1. Verificar instalação do Python
```bash
python3 --version
```

#### 2. Executar os Testes Automatizados
```bash
# Navegue até o diretório do projeto
cd "Verificacao validacao"

# Execute os testes
python3 -m unittest tests.test_user_system -v
```

**Resultado esperado:** 11 testes executados com sucesso ✅


#### 3. Testar o Sistema Manualmente (Opcional)
Crie um arquivo `exemplo_uso.py` na raiz do projeto:

```python
import sys
sys.path.insert(0, 'src')

from user_system import SistemaCadastro

# Cria uma instância do sistema
sistema = SistemaCadastro()

# Testa cadastro válido
sucesso, msg = sistema.cadastrar_usuario("usuario@exemplo.com", "senha123")
print(f"Cadastro 1: {msg}")

# Testa cadastro inválido (e-mail)
sucesso, msg = sistema.cadastrar_usuario("email_invalido", "senha123")
print(f"Cadastro 2: {msg}")

# Testa cadastro inválido (senha)
sucesso, msg = sistema.cadastrar_usuario("teste@exemplo.com", "abc12")
print(f"Cadastro 3: {msg}")

# Busca usuário
usuario = sistema.buscar_usuario("usuario@exemplo.com")
if usuario:
    print(f"Usuário encontrado: {usuario.email}")

# Mostra histórico
print(f"Total de usuários: {sistema.contar_usuarios()}")
```

Execute:
```bash
python3 exemplo_uso.py
```


## Resultados dos Testes

Os testes automatizados validam:
- ✅ Validação de e-mail válido
- ✅ Validação de e-mail inválido
- ✅ Validação de senha válida
- ✅ Validação de senha inválida
- ✅ Cadastro de usuário válido
- ✅ Cadastro com e-mail inválido
- ✅ Cadastro com senha inválida
- ✅ Busca de usuário existente
- ✅ Busca de usuário inexistente
- ✅ Manutenção de histórico de usuários

**Total**: 10 testes automatizados - Todos aprovados ✅

## Documentação

- **Plano de Testes**: Consulte `plano_testes.md` para ver todos os casos de teste detalhados.
- **Código**: Todos os arquivos estão comentados explicando a funcionalidade.

## Observações

- O sistema utiliza `unittest`, que já vem incluído no Python.
- Não são necessárias dependências externas para executar os testes.
- O código está modularizado conforme RNF02.

