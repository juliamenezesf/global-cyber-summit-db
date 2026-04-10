# CP2 - Integração PL/SQL + Python

Projeto desenvolvido para o Checkpoint 2 da FIAP, com foco na integração entre banco de dados Oracle e aplicação web em Python.

---

## 📌 Objetivo

Detectar inscrições fraudulentas no sistema do Global Cyber Summit, utilizando regras de negócio implementadas em PL/SQL e integração com uma interface web.

A interface web envia requisições para uma API em Python (Flask), que executa a lógica PL/SQL diretamente no banco Oracle.

---

## ⚙️ Tecnologias Utilizadas

- Python (Flask)
- Oracle Database
- PL/SQL (Cursor Explícito)
- HTML, CSS e JavaScript

---

## 🚀 Funcionalidades

- Varredura de inscrições com status PENDING
- Identificação de e-mails suspeitos ou inválidos
- Cancelamento automático de inscrições fraudulentas
- Redução do trust_score em 15 pontos
- Registro de auditoria na tabela LOG_AUDITORIA

---

## 🗄️ Estrutura do Projeto

- `app.py` → API Flask responsável pela integração
- `conexao.py` → conexão com o banco Oracle
- `varredura.py` → lógica PL/SQL com cursor explícito
- `index.html` → interface web
- `cp2dados.sql` → script de criação do banco

---

## ▶️ Como Executar (caso queira efetuar o teste de maneira local)

### 🔧 1. Instalar dependências

Abra o terminal na pasta do projeto e execute:

- pip install flask oracledb

---

### 🔐 2. Configurar acesso ao banco

Antes de rodar, você precisa informar os dados do banco Oracle.

No terminal, defina as variáveis de ambiente:
- DB_USER=seu_usuario
- DB_PASSWORD=sua_senha
- DB_DSN=oracle.fiap.com.br:1521/ORCL

(Use suas próprias credenciais do banco)

---
### 🚀 3. Iniciar o backend (API)
Execute:
- python app.py

Se tudo estiver certo, a API ficará rodando localmente.

---

### 🌐 4. Abrir a interface web

Abra o arquivo index.html no navegador.

---

###🔄 5. Ajustar a URL para execução local

No arquivo index.html, verifique se a requisição está apontando para:

- http://127.0.0.1:10000/processar

---

### ▶️ 6. Executar a varredura

No site, clique no botão "Executar Varredura".

---

### 🧪 7. Validar no banco

Após clicar no botão, consulte o banco para verificar:

inscrições com status alterado para CANCELLED
redução do trust_score
registros inseridos na tabela LOG_AUDITORIA

Se essas alterações acontecerem, o sistema está funcionando corretamente.

---

## 📊 Regras de Negócio Implementadas

- Varredura de inscrições com status **PENDING**
- Identificação de e-mails de domínios temporários (*fake.com*, *temp-mail*) ou inválidos
- Cancelamento de inscrições fraudulentas
- Redução do **trust_score** do usuário
- Registro detalhado na tabela **LOG_AUDITORIA**

---

## 👩‍💻 Autoria

Projeto desenvolvido para fins acadêmicos - FIAP (2026).
