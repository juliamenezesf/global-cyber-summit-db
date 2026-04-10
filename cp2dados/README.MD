# CP2 - Integração PL/SQL + Python

Projeto desenvolvido para o Checkpoint 2 da FIAP, com foco na integração entre banco de dados Oracle e aplicação web em Python.

---

## 📌 Objetivo

Detectar inscrições fraudulentas no sistema do Global Cyber Summit, utilizando regras de negócio implementadas em PL/SQL e integração com uma interface web.

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

## 🔐 Configuração do Banco

Antes de executar o projeto, configure suas credenciais no arquivo `conexao.py`:

user="SEU_USUARIO"
password="SUA_SENHA"
dsn="SEU_DSN"

---

## ▶️ Como Executar

1. Instale as dependências:
- pip install flask oracledb

2. Execute a aplicação:
- python app.py

3. Abra o arquivo index.html no navegador e clique em Executar Varredura.

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