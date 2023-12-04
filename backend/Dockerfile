FROM python:3.11.3-slim 

WORKDIR /app

RUN pip install --upgrade pip &&\
    pip install poetry

COPY ../pyproject.toml ../poetry.lock* /app/

# COPY ./backend/.env /app/

# RUN poetry add gunicorn

# RUN poetry install

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

RUN pip install gunicorn==20.1.0

RUN pip install -r requirements.txt --no-cache-dir

COPY ./backend .









# FROM python:3.11.3-slim

# RUN apt-get update &&\
#     apt-get upgrade -y &&\
#     apt-get install -y libpq-dev gcc netcat

# WORKDIR /app

# COPY ./backend .

# COPY --from=requirements-stage /tmp/requirements.txt requirements.txt

# RUN pip install --upgrade pip &&\
#     pip install -r requirements.txt --no-cache-dir

# RUN pip install gunicorn &&\
#     pip install psycopg2-binary

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "prosept_match_product.wsgi"]
