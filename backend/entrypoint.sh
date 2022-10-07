#!/bin/sh

# Wait for the database to be ready
poetry run python /app/app/backend_pre_start.py

# Run the migrations
poetry run alembic upgrade head

# Seed the database
poetry run python /app/app/initial_data.py

exec "$@"
