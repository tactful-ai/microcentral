FROM python:3.9

RUN pip install --upgrade pip

WORKDIR /app
COPY ./requirements.txt .

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean 

RUN pip install -r ./requirements.txt

# Add docker-compose-wait tool -------------------
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait
# -----------------------------------------------

COPY ./app .
COPY ./app/templates /app/
EXPOSE 8000