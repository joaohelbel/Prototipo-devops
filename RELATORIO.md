# Relatório - Protótipo DevOps - API de Produtos com Flask

**Aluno:** João Helbel  
**Data:** 06 de Outubro de 2025  
**Projeto:** API de Produtos com Flask e PostgreSQL containerizados

---

## 1. Resumo do Projeto

Este projeto implementa uma API REST simples usando Flask e PostgreSQL, totalmente containerizada com Docker e orquestrada com docker-compose.

### Tecnologias Utilizadas
- **Flask**: Framework web Python
- **PostgreSQL 13**: Banco de dados relacional
- **Docker**: Containerização
- **Docker Compose**: Orquestração de serviços

---

## 2. Estrutura dos Arquivos Entregues

```
Prototipo-devops/
├── app.py                 # Aplicação Flask
├── requirements.txt       # Dependências Python
├── Dockerfile            # Imagem da aplicação
├── docker-compose.yml    # Orquestração dos serviços
├── init.sql             # Script SQL de inicialização
├── README.md            # Documentação
├── comandos.md          # Comandos de execução
└── .dockerignore        # Otimização do build
```

---

## 3. Comandos Executados e Outputs

### 3.1. Build e Execução dos Containers

**Comando:**
```bash
docker-compose up --build -d
```

**Output:**
```
time="2025-10-06T19:18:44-03:00" level=warning msg="C:\\Users\\joao.helbel\\OneDrive - ESPM\\Documentos\\GitHub\\Prototipo-devops\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"

[+] Building 2.3s (13/13) FINISHED
 => [internal] load local bake definitions                  0.0s 
 => [internal] load build definition from Dockerfile        0.0s 
 => [internal] load metadata for docker.io/library/python:  0.7s 
 => [internal] load .dockerignore                           0.0s 
 => [internal] load build context                           0.0s 
 => [1/6] FROM docker.io/library/python:3.11-slim@sha256:9  0.0s 
 => CACHED [2/6] WORKDIR /app                               0.0s 
 => CACHED [3/6] RUN apt-get update && apt-get install -y   0.0s 
 => CACHED [4/6] COPY requirements.txt .                    0.0s 
 => CACHED [5/6] RUN pip install --no-cache-dir -r require  0.0s 
 => [6/6] COPY app.py .                                     0.0s 
 => exporting to image                                      0.3s 

[+] Running 3/3
 ✔ prototipo-devops-web         Built                       0.0s 
 ✔ Container postgres_produtos  Healthy                     0.9s 
 ✔ Container flask_produtos     Started                     1.2s
```

### 3.2. Verificação dos Containers

**Comando:**
```bash
docker ps -a
```

**Output:**
```
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                    PORTS                      NAMES
fb5d4bfcf710   prototipo-devops-web   "python app.py"          8 minutes ago    Up 8 minutes              0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp   flask_produtos
3cf1eaadcdc7   postgres:13            "docker-entrypoint.s…"   10 minutes ago   Up 10 minutes (healthy)   0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp   postgres_produtos
```

### 3.3. Logs dos Containers

**Comando Flask:**
```bash
docker logs flask_produtos --tail 10
```

**Output:**
```
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.0.3:5000
Press CTRL+C to quit
172.18.0.1 - - [06/Oct/2025 22:20:30] "GET / HTTP/1.1" 200 -
172.18.0.1 - - [06/Oct/2025 22:20:43] "GET /produtos HTTP/1.1" 200 -
172.18.0.1 - - [06/Oct/2025 22:29:16] "GET /produtos HTTP/1.1" 200 -
```

**Comando PostgreSQL:**
```bash
docker logs postgres_produtos --tail 5
```

**Output:**
```
2025-10-06 22:17:19.489 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2025-10-06 22:17:19.496 UTC [63] LOG:  database system was shut down at 2025-10-06 22:17:19 UTC
2025-10-06 22:17:19.503 UTC [1] LOG:  database system is ready to accept connections
```

---

## 4. Configuração do Banco de Dados

### 4.1. Conexão ao PostgreSQL

**Comando:**
```bash
docker exec -it postgres_produtos psql -U postgres
```

### 4.2. Criação do Banco e Tabela

**Comandos SQL executados:**
```sql
CREATE DATABASE aula;
\c aula

CREATE TABLE IF NOT EXISTS produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    preco NUMERIC(10,2) NOT NULL
);

INSERT INTO produtos (nome, preco) VALUES
    ('Teclado', 120.00),
    ('Mouse', 80.00),
    ('Monitor', 900.00),
    ('Headset', 250.00),
    ('Webcam', 180.00);
```

### 4.3. Verificação dos Dados Inseridos

**Comando:**
```sql
SELECT * FROM produtos ORDER BY id;
```

**Output:**
```
 id |  nome   | preco  
----+---------+--------
  1 | Teclado | 120.00
  2 | Mouse   |  80.00
  3 | Monitor | 900.00
  4 | Headset | 250.00
  5 | Webcam  | 180.00
(5 rows)
```

---

## 5. Testes das Rotas da API

### 5.1. Teste da Rota de Saúde

**Comando:**
```bash
curl http://localhost:5000/
```

**Output:**
```
StatusCode        : 200
StatusDescription : OK
Content           : API de Produtos no Docker
Content-Type      : text/html; charset=utf-8
Server            : Werkzeug/3.1.3 Python/3.11.13
```

**Resultado:** ✅ **SUCESSO** - Retorna "API de Produtos no Docker"

### 5.2. Teste da Rota de Produtos

**Comando:**
```bash
curl http://localhost:5000/produtos
```

**Output:**
```
StatusCode        : 200
StatusDescription : OK
Content           : [{"id":1,"nome":"Teclado","preco":120.0},{"id":2,"nome":"Mouse","preco":80.0},{"id":3,"nome":"Monitor","preco":900.0},{"id":4,"nome":"Headset","preco":250.0},{"id":5,"nome":"Webcam","preco":180.0}]
Content-Type      : application/json
Server            : Werkzeug/3.1.3 Python/3.11.13
```

**Resultado:** ✅ **SUCESSO** - Retorna JSON com 5 produtos do banco PostgreSQL

---

## 6. Análise dos Requisitos Atendidos

### 6.1. Requisitos Funcionais ✅
- ✅ **Rota de Saúde**: `GET /` retorna "API de Produtos no Docker"
- ✅ **Rota de Produtos**: `GET /produtos` retorna lista JSON do PostgreSQL
- ✅ **Tabela no Banco**: Criada com `id SERIAL`, `nome VARCHAR(80)`, `preco NUMERIC(10,2)`
- ✅ **Dados**: 5 registros inseridos (mais que os 3 mínimos exigidos)

### 6.2. Requisitos Técnicos ✅
- ✅ **Variáveis de Ambiente**: Todas configuradas (DB_HOST, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD)
- ✅ **Sem Hardcoding**: Nenhuma credencial codificada diretamente
- ✅ **Docker Compose**: Criado do zero, orquestra ambos os serviços
- ✅ **Conectividade**: Rede `produtos_network` permite comunicação
- ✅ **Persistência**: Volume `postgres_data` para dados do PostgreSQL

### 6.3. Arquitetura ✅
- ✅ **Containerização**: Aplicação Flask em container próprio
- ✅ **Separação de Serviços**: Web e banco em containers independentes
- ✅ **Healthcheck**: PostgreSQL com verificação de saúde
- ✅ **Dependências**: Web só inicia após banco estar healthy

---

## 7. Configurações de Rede e Volumes

### 7.1. Rede
```yaml
networks:
  produtos_network:
    driver: bridge
```

### 7.2. Volume
```yaml
volumes:
  postgres_data:
```

### 7.3. Portas Expostas
- **Flask**: `5000:5000`
- **PostgreSQL**: `5432:5432`

---

## 8. Investigação de Erros (Processo de Debug)

Durante o desenvolvimento, alguns erros foram encontrados e resolvidos:

### 8.1. Problema de Autenticação Docker
**Erro:** `authentication required - email must be verified`
**Solução:** Login no Docker Desktop resolveu o problema

### 8.2. Erro de Sintaxe no app.py
**Erro:** `SyntaxError: invalid syntax` - arquivo com conteúdo duplicado
**Solução:** Recriação limpa do arquivo Python

### 8.3. Requirements.txt Corrompido
**Erro:** `No matching distribution found for flask==2.3.3fastapi==0.104.1`
**Solução:** Correção do arquivo requirements.txt

---

## 9. Comandos de Limpeza

Para parar e remover todos os recursos:

```bash
# Parar containers
docker-compose down

# Parar e remover volumes (dados serão perdidos)
docker-compose down -v
```

---

## 10. Conclusão

O projeto foi **implementado com sucesso** atendendo a todos os requisitos:

- ✅ **Aplicação Flask** funcional com 2 rotas
- ✅ **PostgreSQL** com persistência e dados
- ✅ **Docker Compose** orquestrando os serviços
- ✅ **Variáveis de ambiente** configuradas corretamente
- ✅ **Testes** das rotas realizados com sucesso
- ✅ **Documentação** completa fornecida

O protótipo demonstra uma arquitetura de microserviços simples mas funcional, com separação adequada de responsabilidades e uso das melhores práticas de containerização.

---

**Status Final: ✅ PROJETO CONCLUÍDO COM SUCESSO**