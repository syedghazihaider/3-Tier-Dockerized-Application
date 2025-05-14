from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import time
import os

app = Flask(__name__)
CORS(app)  # Enabling CORS globally

DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "mydb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")


def get_db_connection():
    for _ in range(5):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            return conn
        except psycopg2.OperationalError:
            time.sleep(2)
    raise Exception("Unable to connect to the database")


def create_table_if_not_exists():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(users)


@app.route('/add', methods=['POST'])
def add_user():
    data = request.json
    name = data.get("name")
    age = data.get("age")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s) RETURNING id;", (name, age))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"id": new_id, "name": name, "age": age}), 201


# Ensure the 'users' table exists
create_table_if_not_exists()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
