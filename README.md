# microcentral

A Central Hub To Manage And Monitor your microservices against best in class scorecards 

---

## Installation and Running


- Get Docker In your machine you can follow this link to get it in your operating system [install docker](https://docs.docker.com/engine/install/)
- Install Python 3.10+
- Install Poetry
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
- clone the repo.

```bash
git clone https://github.com/tactful-ai/microcentral.git
cd microcentral
```
- create env files
    - `database.env.example => database.env`
    - `app.env.example => app.env`

- Install the dependencies
    
    ```bash 
    sudo apt install libpq-dev gcc
    poetry install
    ```
- Run the following command to create the database

    ```bash
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
