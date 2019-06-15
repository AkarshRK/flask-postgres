Step 1: Install pipenv and pyenv and install Python 3.7.1 using pyenv
Step 2: Create a directory and clone the repository
        - git clone https://github.com/AkarshRK/flask-postgres.git
        - cd flask-postgres

Step 3: Execute the following commands:
        $ pipenv install (this will install the necessary libraries from Pipfile.lock)
        $ pipenv shell (activates virtual env)

Step 4: Install and setup postgres database
        (a) Install postgres:
            $ sudo apt-get update
            $ sudo apt-get install postgresql
        (b) Login to postgres account and create a database:
            - ALTER USER postgres WITH PASSWORD 'postgres';
            - createdb cust_db
            - grant all privileges on cust_db to postgres;
Step 5: Set the following system environment variables
        $ export FLASK_ENV=development
        $ export DATABASE_URL= postgres://name:password@houst:port/blog_api_db
        $ export JWT_SECRET_KEY = klinifyklinify

Step 6: Database Migrations:
        $ python manage.py db init
        $ python manage.py db migrate
        $ python manage.py db upgrade

Step 7: Run your app: $ python run.py

Step 8: Install docker and docker-compose 

Step 9: Build a docker image for "app" and another image for "postgres"
        (a) sudo docker build -t app . (for Dockerfile)
        (b) sudo docker-compose up (for docker-compose.yml)

        


             
            
        

 