FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .
COPY /server ./server
COPY /database ./database

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000