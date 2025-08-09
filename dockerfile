FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD ["uvicorn", "app_api:app", "--host", "0.0.0.0", "--port", "5000"]
