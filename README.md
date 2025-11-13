# Meu Projeto CRUD em Django

Este é um projeto de um sistema de Gerenciamento (CRUD - Create, Read, Update, Delete) desenvolvido em Python com o framework Django.

O sistema foi construído e configurado para rodar em um ambiente GitHub Codespaces e gerencia duas entidades principais: **Funcionários** e **Alimentos**.

Programado por Giovanni Balestra

---

## 🚀 Tecnologias Utilizadas

* **Python**
* **Django** (O framework web)
* **SQLite3** (O banco de dados padrão do Django)
* **GitHub Codespaces** (Ambiente de desenvolvimento)

---

## 📋 Primeiros Passos (Preparando o Ambiente)

Este projeto depende de um arquivo `requirements.txt` para que o Codespaces (ou qualquer outro ambiente) saiba o que instalar.

**Se você ainda não tem um `requirements.txt`:**
1.  Pare o servidor (se estiver rodando).
2.  No terminal, gere o arquivo de dependências:
    ```bash
    pip freeze > requirements.txt
    ```
3.  "Commite" (confirme) este novo arquivo para o seu repositório.

---

## ⚡ Como Executar o Projeto

1.  **Abrir no Codespace:**
    * A forma mais fácil de executar este projeto é abrindo-o diretamente com o GitHub Codespaces.

2.  **Instalar Dependências (Se necessário):**
    * O Codespace deve instalar as dependências do `requirements.txt` automaticamente. Se precisar fazer isso manualmente, rode:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Criar o Banco de Dados (Migrate):**
    * Este comando cria as tabelas `Funcionario` e `Alimento` no arquivo `db.sqlite3`.
    ```bash
    python manage.py migrate
    ```

4.  **Iniciar o Servidor:**
    * Com o banco de dados pronto, inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

5.  **Acessar a Aplicação:**
    * O Codespaces irá notificá-lo para abrir o servidor em uma nova aba do navegador.

---

## ✨ Funcionalidades Atuais

O projeto é um CRUD em desenvolvimento.

### Gerenciamento de Funcionários
* [X] **Create:** Cadastrar um novo funcionário.
* [X] **Read:** Listar todos os funcionários cadastrados.
* [ ] **Update:** (Ainda não implementado)
*