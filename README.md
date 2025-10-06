# Prototipo-devops

API de Produtos Dockerizada com Flask e PostgreSQL

## Descrição

Este projeto é uma API REST simples desenvolvida com Flask e conectada a um banco de dados PostgreSQL, totalmente containerizada com Docker.

## Funcionalidades

- `GET /` - Retorna a mensagem "API de Produtos no Docker"
- `GET /produtos` - Retorna uma lista de produtos em formato JSON do banco de dados

## Estrutura do Banco de Dados

Tabela `produtos`:
- `id` (SERIAL PRIMARY KEY)
- `nome` (VARCHAR(80))
- `preco` (NUMERIC)

## Requisitos

- Docker
- Docker Compose

## Como Usar

1. Clone o repositório:
```bash
git clone https://github.com/joaohelbel/Prototipo-devops.git
cd Prototipo-devops
```

2. Inicie os containers:
```bash
docker compose up --build
```

3. Acesse a API:
- Root endpoint: http://localhost:5000/
- Produtos endpoint: http://localhost:5000/produtos

4. Para parar os containers:
```bash
docker compose down
```

## Estrutura do Projeto

- `app.py` - Aplicação Flask com as rotas da API
- `requirements.txt` - Dependências Python
- `Dockerfile` - Configuração do container Flask
- `docker-compose.yml` - Orquestração dos serviços
- `init.sql` - Script de inicialização do banco de dados
- `.env` - Variáveis de ambiente do banco de dados

## Tecnologias Utilizadas

- Python 3.11
- Flask 3.0.0
- PostgreSQL 15
- Docker & Docker Compose
