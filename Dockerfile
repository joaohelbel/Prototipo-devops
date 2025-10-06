# Use uma imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Instala dependências do sistema necessárias para o PostgreSQL
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY app.py .

# Expõe a porta que a aplicação Flask irá usar
EXPOSE 5000

# Comando para executar a aplicação
CMD ["python", "app.py"]