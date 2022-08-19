# microcentral

Central Hub To Manage And Monitor all service inside [Tactful AI](https://tactful.ai/).

---

## Get Started

to start missing around with the app follow these steps

1. Get Docker In your machine you can follow this link to get it in your operating system [install docker](https://docs.docker.com/engine/install/)

2. clone the repo.

```bash
git clone https://github.com/tactful-ai/microcentral.git
cd microcentral
```

3. create env files

    - `database.env.example => database.env`
    - `app.env.example => app.env`

4. run the following command

```bash
sudo docker-compose up
```

---

For Migrations we went with alembic we after you update the models you need to run theses commands

```bash
sudo docker-compose run --rm app poetry run alembic revision --autogenerate -m "$message"
```

```bash
sudo docker-compose run --rm app poetry run alembic upgrade head
```

and you are good to go

---

those three steps should result you an working app on your localhost

`Enjoy Exploring and issue creating 😁`
