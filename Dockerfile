FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV APP_PORT=8080
ENV DATA_DIR=/data

COPY . .

EXPOSE ${APP_PORT}

CMD ["python", "-m", "app.main"]
