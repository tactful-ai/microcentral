FROM python:3.10

WORKDIR /usr/src/app

# Install Poetry to manage dependencies
RUN pip install poetry
COPY ./pyproject.toml /usr/src/app/pyproject.toml

# Install App dependencies
RUN poetry install


COPY . /usr/src/app
#COPY ./app/templates /app/

# Entrypoint to handle Database Connection & migrations
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]