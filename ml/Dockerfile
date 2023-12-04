FROM python:3.11.3-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt --no-cache-dir

CMD ["python3", "-m", "app"]
