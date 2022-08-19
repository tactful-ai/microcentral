FROM python:3.10

WORKDIR /app
COPY ./pyproject.toml .

# Install System dependencies
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean 

# Install Poetry to manage dependencies
RUN pip install poetry

# Install App dependencies
RUN poetry install


COPY ./app .
COPY ./app/templates /app/
EXPOSE 8000