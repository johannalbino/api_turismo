# Pega a imagem do debian com o python3 instalado
FROM python:3.8-slim-buster

# Remove o delay do log
ENV PYTHONUNBUFFERED 1

# Cria a pasta do projeto /code
WORKDIR /srv

# Adiciona o requirements.txt na pasta code
ADD Pipfile* ./

# Instala as dependencias do projeto no docker
RUN pip install --no-cache -U pip pipenv && pipenv install --system

# Adicionar o código no /code/
ADD . /srv/

ENTRYPOINT ["python", "manage.py"]
