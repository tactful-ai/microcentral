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
