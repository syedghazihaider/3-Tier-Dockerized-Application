FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip   # This line upgrades pip
RUN apt-get update && apt-get install -y libpq-dev  # Important for PostgreSQL
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
