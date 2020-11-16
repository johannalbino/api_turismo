# Listagem de Vitrines

Objetivo desta API é listar as vitrinas para um website (front-end), ele tem o metodo de get e post, ambos servindo para listar vitrines.


Metódos:

* GET:
    
Esse metodo vai retornar todos as vitrines disponiveis
    
* POST '/vitrines':
    
Esse metodo é necessário um paylod ou um body na requisição. Exemplo de body:

        {
            "routes": ["/sobre"]
        }

No exemplo acima vai retornar os dados de sobre.

# Como executar o projeto com docker

Pré-requisito:
    
    Docker

* criar o arquivo .env igual o .env-dev que se encontra na raiz do projeto
* executar o comando:
    
        docker-compose up --build
        

# Como executar o projeto localmente

Pré-requisito:

    postgres
    python3.8.5
    pip

Instalar:
    
    pip install pipenv
    pipenv install
    pipenv shell
    
* Criar a database no seu banco local
* Criar o arquivo .env semelhante ao .env-dev, porém deve informar as credenciais do seu banco de dados.
* Rodar o migrate do projeto para criar as tabelas do banco de dados.
    
    python manage.py migrate
    
* Executar o projeto:
    
    python manage.py runserver
    
    
Enpoints:

    GET /vitrines?limit=1 - Vai retornar apenas um dado.
    POST /vitrines - Deve informar o body