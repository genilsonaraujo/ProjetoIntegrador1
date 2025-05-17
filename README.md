# Gerenciador de Estoque 

![Lista de Produtos](projetointegradors/static/lista.png)

## Overview

O Gerenciador de Produtos é uma aplicação web desenvolvida utilizando o framework Django. Este sistema tem como objetivo auxiliar a "Paloma Comércio de Parafusos e Materiais em Geral" no gerenciamento eficiente de seu estoque, proporcionando funcionalidades essenciais e uma solução acessível.

## Funcionalidades Principais

- **Autenticação de Usuários:** Sistema seguro com autenticação de usuários para garantir acesso controlado.

- **Catálogo de Produtos:** Lista completa de produtos disponíveis na loja.

- **Edição de Informações:** Capacidade de editar informações de produtos para manter o catálogo atualizado.

- **Controle de Vendas (em desenvolvimento):** Funcionalidade para controle de vendas e geração de relatórios (em fase de implementação).

## Problema Abordado

O principal desafio enfrentado pela "Paloma Comércio de Parafusos e Materiais em Geral" é a falta de opções de gerenciadores de estoque acessíveis no mercado. Ferramentas tradicionais muitas vezes apresentam custos proibitivos para pequenos empreendimentos, o que motivou o desenvolvimento deste sistema para atender às necessidades específicas do negócio.

## Pré-requisitos

- Python (versão x.x.x)
- Django (versão x.x.x)

## Como Instalar e Executar

<p>1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/paloma-commerce-inventory.git
cd paloma-commerce-inventory
Crie e ative um ambiente virtual (opcional, mas recomendado):
bash
Copy code
python -m venv env
source env/bin/activate  # no Windows, use "env\Scripts\activate"
Instale as dependências:
bash
Copy code
pip install -r requirements.txt
Aplique as migrações:
bash
Copy code
python manage.py migrate
Execute o servidor local:
bash
Copy code
python manage.py runserver
Acesse a aplicação em http://localhost:8000 no seu navegador.</p>

#Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

#Licença
Este projeto é distribuído sob a licença [Nome da Licença]. Veja o arquivo LICENSE.md para mais detalhes.



# Paloma Comércio - Gerenciador de Estoque

Este projeto é um Sistema de Gestão de Estoque desenvolvido para a "Paloma Comércio de Parafusos e Materiais em Geral". A aplicação é construída utilizando o framework Django e tem como objetivo proporcionar uma solução eficiente e acessível para o controle de estoque de pequenos empreendimentos.

## Funcionalidades

- Autenticação de Usuários
- Listagem de Produtos
- Adição e Edição de Produtos
- [Outras funcionalidades...]

## Screenshots

### Tela de Login
![Tela de Login](/imagens/login.png)

### Lista de Produtos
![Lista de Produtos](/imagens/lista_produtos.png)

### Adicionar Produto
![Adicionar Produto](/imagens/adicionar_produto.png)

### Editar Produto
![Adicionar Produto](/imagens/editar_produto.png)

### Tela do Banco de Dados (SQL)
![Tela do Banco de Dados](/imagens/db_sql.png)

## Como Executar o Projeto

1. Clone o repositório: `git clone https://github.com/seu-usuario/nome-do-repositorio.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute as migrações do banco de dados: `python manage.py migrate`
4. Inicie o servidor: `python manage.py runserver`

## Contribuições

Contribuições são bem-vindas! Por favor, siga as diretrizes de contribuição.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
