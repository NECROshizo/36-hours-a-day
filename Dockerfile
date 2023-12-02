FROM python:3.11.3-slim as requirements-stage

WORKDIR /tmp

RUN pip install --upgrade pip &&\
    pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11.3-slim

RUN apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install -y libpq-dev gcc netcat

WORKDIR /app

COPY ./backend .

COPY --from=requirements-stage /tmp/requirements.txt requirements.txt

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt --no-cache-dir

RUN pip install gunicorn &&\
    pip install psycopg2-binary

CMD ["gunicorn", "--bind", "0:8000", "prosept_match_product.wsgi"]
