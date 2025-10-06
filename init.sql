-- Script SQL para criar e popular a tabela de produtos
-- Execute este script após conectar ao container PostgreSQL

-- Conectar ao banco 'aula'
\c aula

-- Criar tabela produtos
CREATE TABLE IF NOT EXISTS produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    preco NUMERIC(10,2) NOT NULL
);

-- Inserir dados de exemplo
INSERT INTO produtos (nome, preco) VALUES
    ('Teclado', 120.00),
    ('Mouse', 80.00),
    ('Monitor', 900.00),
    ('Headset', 250.00),
    ('Webcam', 180.00);

-- Verificar os dados inseridos
SELECT * FROM produtos ORDER BY id;