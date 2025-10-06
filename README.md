# Protótipo DevOps - API de Produtos com Flask# Protótipo DevOps - API de Produtos



Este projeto implementa uma API REST simples usando Flask e PostgreSQL, containerizada com Docker.Projeto desenvolvido para avaliar habilidades em:

- Execução de containers Docker

## Arquitetura- Operação de PostgreSQL com persistência

- Containerização de aplicação web (FastAPI)

- **Flask**: Framework web Python para a API- Orquestração com docker-compose

- **PostgreSQL**: Banco de dados relacional para armazenar produtos

- **Docker**: Containerização da aplicação## 🚀 Tecnologias

- **Docker Compose**: Orquestração dos serviços

- **FastAPI** - Framework web moderno para Python

## Estrutura do Projeto- **PostgreSQL** - Banco de dados relacional

- **Docker** - Containerização

```- **Docker Compose** - Orquestração de containers

.

├── app.py                 # Aplicação Flask## 📋 Funcionalidades

├── requirements.txt       # Dependências Python

├── Dockerfile            # Imagem da aplicação- **GET /** - Endpoint de saúde que retorna `{"message": "API de Produtos com FastAPI"}`

├── docker-compose.yml    # Orquestração dos serviços- **GET /produtos** - Lista todos os produtos do banco PostgreSQL

├── init.sql             # Script SQL de inicialização

├── comandos.md          # Comandos para execução## 🛠 Como executar

└── README.md            # Este arquivo

```### 1. Pré-requisitos

- Docker

## Funcionalidades- Docker Compose



### Rotas da API### 2. Clonar o repositório

```bash

1. **Rota de Saúde**git clone https://github.com/joaohelbel/Prototipo-devops.git

   - `GET /` → Retorna: "API de Produtos no Docker"cd Prototipo-devops

```

2. **Rota de Produtos**

   - `GET /produtos` → Retorna lista de produtos do PostgreSQL### 3. Executar com Docker Compose

```bash

### Banco de Dados# Construir e subir todos os serviços

docker-compose up --build -d

Tabela `produtos`:

- `id` (SERIAL PRIMARY KEY)# Verificar se os containers estão rodando

- `nome` (VARCHAR(80))docker-compose ps

- `preco` (NUMERIC(10,2))```



Dados de exemplo:### 4. Configurar o banco de dados

- Teclado - R$ 120,00```bash

- Mouse - R$ 80,00  # Entrar no container do PostgreSQL

- Monitor - R$ 900,00docker exec -it postgres_produtos psql -U postgres



## Como Executar# Executar o script SQL (dentro do psql)

\i /init.sql

### Pré-requisitos```

- Docker

- Docker ComposeOu executar o script diretamente:

```bash

### Passosdocker exec -i postgres_produtos psql -U postgres < init.sql

```

1. **Clonar o repositório**

```bash### 5. Testar a API

git clone <url-do-repo>

cd Prototipo-devops**Endpoint de saúde:**

``````bash

curl http://localhost:8000/

2. **Subir os containers**# Resposta: {"message":"API de Produtos com FastAPI"}

```bash```

docker-compose up --build -d

```**Listagem de produtos:**

```bash

3. **Verificar se os containers estão rodando**curl http://localhost:8000/produtos

```bash# Resposta: [{"id":1,"nome":"Teclado","preco":120.0}, ...]

docker ps```

```

Ou acessar diretamente no navegador:

4. **Executar o script SQL para criar a tabela**- http://localhost:8000/ 

```bash- http://localhost:8000/produtos

docker exec -it postgres_produtos psql -U postgres- http://localhost:8000/docs (Documentação automática do FastAPI)

```

No prompt psql:## 🗃 Estrutura do Projeto

```sql

CREATE DATABASE aula;```

\c aula├── app.py              # Aplicação FastAPI

CREATE TABLE IF NOT EXISTS produtos (├── requirements.txt    # Dependências Python

  id SERIAL PRIMARY KEY,├── Dockerfile         # Imagem Docker da aplicação

  nome VARCHAR(80) NOT NULL,├── docker-compose.yml # Orquestração dos serviços

  preco NUMERIC(10,2) NOT NULL├── init.sql          # Script de inicialização do banco

);├── COMANDOS.md       # Guia de comandos úteis

INSERT INTO produtos (nome, preco) VALUES└── README.md         # Este arquivo

('Teclado', 120.00),```

('Mouse', 80.00),

('Monitor', 900.00);## 🐘 Banco de Dados

SELECT * FROM produtos ORDER BY id;

\q**Tabela: produtos**

```- `id` (SERIAL PRIMARY KEY)

- `nome` (VARCHAR(80))  

5. **Testar a aplicação**- `preco` (NUMERIC(10,2))

```bash

# Rota de saúde**Dados de exemplo:**

curl http://localhost:5000/- Teclado - R$ 120,00

- Mouse - R$ 80,00

# Rota de produtos  - Monitor - R$ 900,00

curl http://localhost:5000/produtos- Headset - R$ 250,00

```- Webcam - R$ 180,00



## Configuração## 🔧 Configurações



### Variáveis de AmbienteA aplicação utiliza variáveis de ambiente para configuração:

- `DB_HOST=db` (nome do serviço no docker-compose)

A aplicação utiliza as seguintes variáveis de ambiente:- `POSTGRES_DB=aula`

- `POSTGRES_USER=postgres`

- `DB_HOST`: Host do banco (padrão: "db")- `POSTGRES_PASSWORD=123456`

- `POSTGRES_DB`: Nome do banco (padrão: "aula")

- `POSTGRES_USER`: Usuário do banco (padrão: "postgres")## 📊 Monitoramento

- `POSTGRES_PASSWORD`: Senha do banco (padrão: "123456")

- `POSTGRES_PORT`: Porta do banco (padrão: "5432")```bash

# Ver logs de todos os serviços

### Portasdocker-compose logs



- **Flask**: 5000:5000# Ver logs específicos

- **PostgreSQL**: 5432:5432docker-compose logs web

docker-compose logs db

### Volumes

# Status dos containers

- `postgres_data`: Volume nomeado para persistência dos dados do PostgreSQL em `/var/lib/postgresql/data`docker-compose ps

docker ps -a

## Comandos Úteis```



```bash## 🛑 Parar os serviços

# Ver logs da aplicação

docker logs flask_produtos```bash

# Parar todos os serviços

# Ver logs do bancodocker-compose down

docker logs postgres_produtos

# Parar e remover volumes (remove dados do banco)

# Parar os containersdocker-compose down -v

docker-compose down```



# Parar e remover volumes## 📝 Notas Técnicas

docker-compose down -v

- A aplicação aguarda o PostgreSQL estar pronto através de healthcheck

# Reconstruir imagens- Volume nomeado `postgres_data` garante persistência dos dados

docker-compose build --no-cache- Rede `produtos_network` permite comunicação entre containers

```- Retry automático na conexão com o banco para maior confiabilidade

## Resolução de Problemas

1. **Erro de conexão com banco**: Aguarde alguns segundos após subir os containers para o PostgreSQL inicializar completamente.

2. **Porta já em uso**: Altere as portas no `docker-compose.yml` se necessário.

3. **Problemas de permissão**: No Linux/Mac, pode ser necessário usar `sudo` com os comandos Docker.

## Tecnologias Utilizadas

- **Python 3.11**
- **Flask 2.3.3**
- **PostgreSQL 15**
- **psycopg2-binary 2.9.7**
- **Docker & Docker Compose**