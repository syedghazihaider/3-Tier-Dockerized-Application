from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import time

app = Flask(__name__)
CORS(app)

def get_db_connection():
    for _ in range(5):
        try:
            conn = psycopg2.connect(
                host="db",
                database="mydb",
                user="postgres",
                password="password"
            )
            return conn
        except psycopg2.OperationalError:
            time.sleep(2)
    raise

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

create_table_if_not_exists()

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, age) VALUES (%s, %s)",
        (data['name'], data['age'])
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Data added successfully!"})

@app.route('/')
def hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    users = [{"id": row[0], "name": row[1], "age": row[2]} for row in rows]
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

