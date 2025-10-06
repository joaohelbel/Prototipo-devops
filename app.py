import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "aula")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "123456")
DB_PORT = int(os.getenv("POSTGRES_PORT", "5432"))

def get_conn():
    return psycopg2.connect(
        host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT
    )

@app.route("/", methods=["GET"])
def health():
    return "API de Produtos no Docker", 200

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, nome, preco FROM produtos ORDER BY id;")
            rows = cur.fetchall()
    dados = [{"id": r[0], "nome": r[1], "preco": float(r[2])} for r in rows]
    return jsonify(dados), 200

if __name__ == "__main__":
    # Em container, use host 0.0.0.0 e porta 5000
    app.run(host="0.0.0.0", port=5000)