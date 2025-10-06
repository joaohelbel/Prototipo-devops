# Comandos para executar o projeto# Guia de Comandos - Protótipo DevOps



## 1. Construir e subir os containers## 1. Construir e executar os containers

docker-compose up --build -d```bash

# Construir e subir todos os serviços

## 2. Verificar se os containers estão rodandodocker-compose up --build -d

docker ps

# Ver status dos containers

## 3. Aguardar o banco inicializar e executar o script SQLdocker-compose ps

# Aguarde alguns segundos após o comando acima, depois execute:docker ps -a

docker exec -it postgres_produtos psql -U postgres -d aula -f /init.sql```



## Ou executar os comandos SQL manualmente:## 2. Verificar logs

docker exec -it postgres_produtos psql -U postgres```bash

# No prompt psql, execute:# Logs de todos os serviços

# CREATE DATABASE aula;docker-compose logs

# \c aula

# CREATE TABLE IF NOT EXISTS produtos (id SERIAL PRIMARY KEY, nome VARCHAR(80) NOT NULL, preco NUMERIC(10,2) NOT NULL);# Logs específicos

# INSERT INTO produtos (nome, preco) VALUES ('Teclado', 120.00), ('Mouse', 80.00), ('Monitor', 900.00);docker-compose logs web

# SELECT * FROM produtos ORDER BY id;docker-compose logs db

```

## 4. Testar as rotas da aplicação

# Rota de saúde:## 3. Executar o script SQL no PostgreSQL

curl http://localhost:5000/```bash

# Entrar no container do banco

# Rota de produtos:docker exec -it postgres_produtos psql -U postgres

curl http://localhost:5000/produtos

# Ou executar o script diretamente

## 5. Verificar logs dos containersdocker exec -i postgres_produtos psql -U postgres < init.sql

docker logs flask_produtos```

docker logs postgres_produtos

## 4. Testar a API

## 6. Para parar os containers```bash

docker-compose down# Testar endpoint de saúde

curl http://localhost:8000/

## 7. Para parar e remover tudo (incluindo volumes)

docker-compose down -v# Testar listagem de produtos
curl http://localhost:8000/produtos
```

## 5. Parar e limpar
```bash
# Parar os serviços
docker-compose down

# Parar e remover volumes (CUIDADO: remove dados)
docker-compose down -v
```

## 6. Comandos úteis para debugging
```bash
# Entrar no container da aplicação
docker exec -it fastapi_produtos /bin/bash

# Verificar conectividade entre containers
docker exec -it fastapi_produtos ping db

# Ver informações detalhadas dos containers
docker inspect postgres_produtos
docker inspect fastapi_produtos
```