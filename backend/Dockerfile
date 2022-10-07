FROM python:3.10

WORKDIR /app

# Install Poetry to manage dependencies
RUN pip install poetry
COPY ./pyproject.toml /app/pyproject.toml

# Install App dependencies
RUN poetry install

# Copy the rest of the app
COPY . /app

# Entrypoint to handle Database Connection & migrations
ENTRYPOINT ["/app/entrypoint.sh"]
ENV PYTHONPATH=/app
