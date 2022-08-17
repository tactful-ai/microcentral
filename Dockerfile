FROM python:3.10

RUN pip install --upgrade pip

WORKDIR /app
COPY ./pyproject.toml .

RUN apt-get update \
    && apt-get install gcc curl -y \
    && apt-get clean 

#RUN curl -sSL https://install.python-poetry.org/ | python -

RUN pip install poetry
RUN poetry install --no-root --remove-untracked


COPY ./app .
COPY ./app/templates /app/
EXPOSE 8000