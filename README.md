PyVendas é um sistema simples em Python para gerenciar produtos com login e CRUD (Criar, Ler, Atualizar, Deletar). Usa MySQL para armazenar dados e colorama para uma interface CLI colorida.


Funcionalidades
Registro de Usuários: Cadastre novos usuários com nome, email e senha (criptografada com SHA-256).
Login Seguro: Autenticação com limite de tentativas para acessar o sistema.
CRUD de Produtos:
Criar: Adicione produtos com nome e valor.
Ler: Visualize todos os produtos cadastrados.
Atualizar: Edite nome e valor de produtos existentes.
Deletar: Remova produtos pelo ID.
Interface de linha de comando (CLI) colorida com colorama.

Pré-requisitos
Python 3.8 ou superior
MySQL 8.0 ou superior
Bibliotecas Python:
mysql-connector-python
colorama
getpass (já incluído no Python)

Como utilizar:
Clone o repositorio
Baixe as dependencias
Configure o banco de dados

Uso
Ao iniciar, escolha entre:
[1] Entrar: Faça login com um usuário existente.
[2] Registrar: Crie um novo usuário.

Após o login, use o menu CRUD:
[1] Adicionar produto
[2] Ver produtos
[3] Atualizar produto
[4] Remover produto
[5] Sair

[Ryan Moscardini] - [ryanoliveiramosc.com.098@gmail.com]
