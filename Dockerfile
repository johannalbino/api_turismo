# Pega a imagem do debian com o python3 instalado
FROM python:3.8-slim-buster

# Remove o delay do log
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-psycopg2 \
    libpq-dev \
    python3-dev \
    postgresql-server-dev-all

# Cria a pasta do projeto /code
WORKDIR /srv

# Adiciona o requirements.txt na pasta code
ADD Pipfile* ./

# Instala as dependencias do projeto no docker
RUN pip install --no-cache -U pip pipenv && pipenv install --system

# Adicionar o código no /code/
ADD . /srv/

RUN chmod +x ./app.sh

ENTRYPOINT ["./app.sh"]
