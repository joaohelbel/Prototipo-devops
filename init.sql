CREATE TABLE IF NOT EXISTS produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    preco NUMERIC(10, 2) NOT NULL
);

INSERT INTO produtos (nome, preco) VALUES
    ('Notebook', 3500.00),
    ('Mouse', 50.00),
    ('Teclado', 150.00);
