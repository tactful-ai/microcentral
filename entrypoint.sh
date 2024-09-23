#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Run migrations to create tables
#poetry run python app/manager.py init_db
echo "Running migrations..."
poetry run alembic revision --autogenerate -m "Initial migration"
echo "Revision created"
poetry run alembic upgrade head
echo "Migrations complete"

# Seed the database
poetry run python /app/app/initial_data.py

exec "$@"
