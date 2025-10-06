from flask import Flask, jsonify
import psycopg2
import os
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=os.getenv('DB_PORT', 5432)
    )
    return conn

@app.route('/')
def index():
    return "API de Produtos no Docker"

@app.route('/produtos')
def produtos():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM produtos;')
    produtos = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(produtos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
