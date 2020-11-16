#!/bin/bash

echo "Esperando o banco de dados conectar"
postgres_ready() {
python3 << END
import sys
import psycopg2
import os
try:
    conn = psycopg2.connect(
      dbname=os.environ.get('NAME', 'turismo'),
      user=os.environ.get('USER', 'turismo'),
      password=os.environ.get('PASSWORD', 'turismo'),
      host=os.environ.get('HOST', 'postgres')
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "PostgreSQL não está disponível ainda - Espere..."
  sleep 1
done

echo "Rodando as migrações"
python3 manage.py migrate

echo "Rodando as fixtures"
python3 manage.py loaddata fixtures

echo "Validando flake8"
flake8

echo "Rodando o servidor"
gunicorn turismo.wsgi -b 0.0.0.0:8000 --reload --graceful-timeout=300 --timeout=300 --log-level DEBUG --workers 1
