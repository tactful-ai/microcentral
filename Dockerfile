FROM python:3.9

RUN pip install --upgrade pip

WORKDIR /app
COPY ./requirements.txt .

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean 

RUN pip install -r ./requirements.txt

COPY ./app .
COPY ./app/templates /app/
EXPOSE 8000