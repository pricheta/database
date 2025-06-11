FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .
COPY alembic.ini .
COPY migration/ ./migration
COPY database/ ./database


CMD ["sh", "-c", "alembic upgrade head"]