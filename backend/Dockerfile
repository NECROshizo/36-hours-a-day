FROM python:3.11.3-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY . .

RUN pip install gunicorn==20.1.0

RUN pip install -r requirements.txt --no-cache-dir


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "prosept_match_product.wsgi"]
