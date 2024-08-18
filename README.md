# microcentral

A Central Hub To Manage And Monitor your microservices against best in class scorecards 

---

## Installation and Running on local machine

- Get Docker In your machine you can follow this link to get it in your operating system [install docker](https://docs.docker.com/engine/install/)
- Install Python 3.10+


    ```bash
    curl -sSL https://install.python-poetry.org | python3 -

    # Install the dependencies
    sudo apt install libpq-dev gcc
    poetry install

    # run database inside docker 
    docker-compose up -d database

    # then run the migrations
    poetry run alembic upgrade head

    # seed some data (services, teams, scorecards)
    poetry run python -m app.initial_data

    # then run the app fastapi
    poetry run fastapi dev
    
    ```



## Running on a Server using Docker Compose

4. run the following command

```bash
sudo docker-compose up

# For Migrations we went with alembic we after you update the models you need to run theses commands
sudo docker-compose run --rm app poetry run alembic revision --autogenerate -m "$message"
sudo docker-compose run --rm app poetry run alembic upgrade head
# and you are good to go
```

```
## Installation and Running on local machine

- Get Docker In your machine you can follow this link to get it in your operating system [install docker](https://docs.docker.com/engine/install/)
- Install Python 3.10+


    ```bash
    curl -sSL https://install.python-poetry.org | python3 -

    # Install the dependencies
    sudo apt install libpq-dev gcc

    poetry install
        Package operations: 40 installs, 0 updates, 0 removals

        - Installing idna (3.7)
        - Installing mdurl (0.1.2)
        - Installing sniffio (1.3.1)
        - Installing anyio (4.4.0)
        - Installing colorama (0.4.6)
        - Installing markdown-it-py (3.0.0)
        - Installing pygments (2.18.0)
        - Installing certifi (2024.7.4)
        - Installing click (8.1.7)
        - Installing h11 (0.14.0)
        - Installing httptools (0.6.1)
        - Installing python-dotenv (1.0.1)
        - Installing pyyaml (6.0.2)
        - Installing rich (13.7.1)
        - Installing shellingham (1.5.4)
        - Installing typing-extensions (4.12.2)
        - Installing watchfiles (0.23.0)
        - Installing websockets (12.0)
        - Installing annotated-types (0.7.0)
        - Installing dnspython (2.6.1)
        - Installing httpx (0.27.0)
        - Installing jinja2 (3.1.4)
        - Installing mako (1.3.5)
        - Installing pydantic (2.8.2)
        - Installing python-multipart (0.0.9)
        - Installing sqlalchemy (1.4.53)
        - Installing starlette (0.37.2)
        - Installing alembic (1.13.2)
        - Installing fastapi (0.111.1)
        - Installing psycopg2 (2.9.9)
        - Installing pydantic-settings (2.4.0)
        - Installing pyjwt (2.9.0)


    # run database inside docker 
    docker-compose up -d database

    # generate migrations initial version
    poetry run alembic revision --autogenerate -m "$message"

    # then run the migrations
    poetry run alembic upgrade head

    # seed some data (services, teams, scorecards)
    poetry run python -m app.initial_data

    # then run the app fastapi
    poetry run fastapi dev
```