# 3-Tier Dockerized Application

This is a 3-tier Dockerized application consisting of:

1. **Frontend** — React.js
2. **Backend** — Flask (Python)
3. **Database** — PostgreSQL

All three components are containerized using Docker and managed with Docker Compose for orchestration.

---

## 🗂️ **Directory Structure**

```
3tier-app/
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│   ├── package.json
│   └── package-lock.json
│
├── docker-compose.yml
└── README.md
```

---

## 🚀 **Setup Instructions**

1️⃣ **Clone the Repository:**

```bash
git clone <your-repo-url>
cd 3tier-app
```

2️⃣ **Build and Run the Application:**

```bash
docker compose up -d
```

3️⃣ **Access the Application:**

* Frontend: [http://localhost:3000](http://localhost:3000)
* Backend Health Check: [http://localhost:5000](http://localhost:5000)
* Get All Users API: [http://localhost:5000/users](http://localhost:5000/users)

---

## 🗃️ **Database Setup**

To create the `users` table in PostgreSQL:

```bash
docker compose exec db psql -U postgres -d mydb -c "CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(50), age INT);"
```

---

## 🔄 **Persistent Data Storage**

The database is connected to a Docker Volume, ensuring data is not lost even after restarting Docker Compose.

Volume configuration in `docker-compose.yml`:

```yaml
volumes:
  pgdata:
```

---

## 🌐 **Docker Compose Configuration**

The `docker-compose.yml` file sets up three services:

* **frontend** → React Application
* **backend** → Flask REST API
* **db** → PostgreSQL Database

They all communicate over a shared Docker network: `app-network`.

---

## 🛠️ **Technologies Used**

* **Docker & Docker Compose**
* **React.js** for Frontend
* **Flask (Python)** for Backend
* **PostgreSQL** for Database

---

## ✅ **Best Practices Followed**

* Docker Compose for Service Management
* Environment Variables for Configuration
* Docker Volumes for Persistent Storage
* Shared Docker Network for Communication

---

## 👨‍💻 **Contributors**

* Syed Ghazi Haider

Feel free to contribute and open issues for improvements!

---
