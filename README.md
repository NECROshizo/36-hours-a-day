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
2. Создание и активация виртуального окружения при помощи [poetry](https://python-poetry.org/docs/#installation)
    ```bash
    poetry env use python
    poetry install
    poetry shell
    ```
> **Примечание:** версия python должна быть 3.12

3. Инициализация [pre-commit](#технологии).
   ```bash
   poetry run pre-commit install
   ```

### Инфраструктура:

docker-compose для запуска postgress в docker:
```bash
docker compose --env-file .env -f infra/docker-compose.infra.yml up -d
```
для него нужен .env по шаблону .env.example

### Шпаргалки
<details>
  <summary><h3>Команды poetry</h3></summary>

- Создание нового проекта: `poetry new new_project`
- Запуск виртуального окружения: `poetry shell`
- Внедрение Poetry в уже имеющийся проект: `poetry init`
- Обновление зависимостей: `poetry update`
- Добавление новой библиотеки: `poetry add <имя_библиотеки>`
- Удаление зависимости: `poetry remove <имя_библиотеки>`
- Просмотр зависимостей: `poetry show`
- Запуск из виртуального окружения: `poetry run <команда>`

</details>

<details>
  <summary><h3>Команды pre-commit</h3></summary>

  **Важно** С использованием poetry, выполнение команд из виртуального окружения происходит через `poetry run <команда>`.
- Установить pre-commit в проекте: `pre-commit install`
- Запустить проверку всех хуков: `pre-commit run -a`
- Запустить конкретный хук: `poetry run pre-commit run <имя-хука>`
- Деактивировать автоматическое выполнение хуков перед коммитом: `poetry run pre-commit uninstall`
- Обновить pre-commit хуки: `poetry run pre-commit autoupdate`

</details>
