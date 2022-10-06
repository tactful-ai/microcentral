#!/bin/sh

##if [ "$DATABASE" = "postgres" ]
##then
#    echo "Waiting for postgres..."

#    while ! nc -z $SQL_HOST $SQL_PORT; do
#      sleep 0.1
#    done

#    echo "PostgreSQL started"
##fi

# Run migrations to create tables

poetry run python /app/app/backend_pre_start.py

poetry run alembic upgrade head

poetry run python /app/app/initial_data.py

exec "$@"
