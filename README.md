# 36-hours-a-day
Командны [проект](http://81.31.246.11/) в рамках Хакатона Просепт. Выполнин командой № 14.
### Технологии
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/Node.js-20-339933?style=flat&logo=node.js&logoColor=white)](https://nodejs.org/)
[![Django](https://img.shields.io/badge/Django-3.2.10-blue?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/DRF-3.12.4-blue?style=flat&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![React](https://img.shields.io/badge/React-11.11.1-61DAFB?style=flat&logo=react&logoColor=white)](https://reactjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/Nginx-1.25.3-009639?style=flat&logo=nginx&logoColor=white)](https://nginx.org/)
[![Docker](https://img.shields.io/badge/Docker-latest-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
---
[![Ruff](https://img.shields.io/badge/Ruff-used-green?style=flat&logo=python&logoColor=white)](https://docs.astral.sh/ruff/)

библиотеки и технологии для [backend](https://github.com/NECROshizo/36-hours-a-day-backend/blob/main/backend/requirements.txt) для [frontend](https://github.com/NECROshizo/36-hours-a-day-backend/blob/main/frontend/package.json) и для [ML](https://github.com/NECROshizo/36-hours-a-day-backend/blob/main/ml/requirements.txt)
### Настройка и запуск локально для разработки
1. Клонировать репозиторий.
    ```bash
    git clone git@github.com:NECROshizo/36-hours-a-day-backend.git
    cd 36-hours-a-day-backend
    ```
2. Необходимо создать ваил .env по шаблону [.env.example](https://github.com/NECROshizo/36-hours-a-day-backend/blob/main/infra/.env.example)

3. Запуск локально
    ```bash
    docker compose -f infra/docker-compose.local.yml up -d
    ```
### Дополнительная информация:
1. Динамическая документация openAPI [swagger](http://81.31.246.11/swagger/)
2. Настройки ML по умолчанию стоят на зупуск поиска соответствий 23:30:15 UTC+3, каждого дня. Изменяются в файле [settings.py](https://github.com/NECROshizo/36-hours-a-day-backend/blob/main/ml/setting.py) перед запуском проекта.

### Состав команды №14 "36 часов в сутках"
Проджект-менеджер: Лера Рослова

DS: [Анастасия Крицкая](https://github.com/avkrickaya), [Иван Прошин](https://github.com/Shakal-tabaki), [Олеся Круглова](https://github.com/zdesia)

Frontend: [Анастасия Пашкова](https://github.com/Malkusha)

Backend: [Антон Лучик](https://github.com/Intemic), [Пётр Оганин](https://github.com/NECROshizo)

2023 г.
