# 36-hours-a-day

### Технологии
[![Django](https://img.shields.io/badge/Django-3.2.10-blue?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/DRF-3.12.4-blue?style=flat&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
---
[![Ruff](https://img.shields.io/badge/Ruff-used-green?style=flat&logo=python&logoColor=white)](https://docs.astral.sh/ruff/)

### Настройка и запуск локально для разработки
Проект использует [Poetry](https://python-poetry.org/) как инструмент управления зависимостями.
1. Клонировать репозиторий.
    ```bash
    git clone git@github.com:NECROshizo/36-hours-a-day-backend.git
    cd 36-hours-a-day-backend
    ```
2. Создание и активация виртуального окружения 
    ```bash
    cd backend
    python -m ven venv
    . venv/bin/activate(Linux) или . venv/Script/activate(Windows)
    pip install -r requirements.txt
    ```

### Инфраструктура:
запуск локально(при активированом виртуальном окружении):
  ```bash
  python manage.py runserver
  ```
или запуск в контейнерах(пока не настроен)

docker-compose для запуска postgress в docker:
```bash
docker compose --env-file .env -f infra/docker-compose.infra.yml up -d
```
нужен .env по шаблону .env.example в папке backend
