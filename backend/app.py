from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import time

app = Flask(__name__)
CORS(app)
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
<<<<<<< HEAD
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

=======
            time.sleep(2)  
    raise Exception("Database connection failed")
>>>>>>> 240c12d (Removed nested Git repo and staged changes)
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

@app.route('/')
def hello():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
