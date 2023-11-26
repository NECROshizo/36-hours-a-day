# 36-hours-a-day

### Технологии
[![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.20-blue?style=flat&logo=python&logoColor=white)](https://pypi.org/project/SQLAlchemy/2.0.20/)
[![Alembic](https://img.shields.io/badge/Alembic-1.12.0-blue?style=flat&logo=python&logoColor=white)](https://pypi.org/project/Alembic/1.12.0/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.3.0-blue?style=flat&logo=python&logoColor=white)](https://pypi.org/project/Pydantic/2.3.0/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.103.1-blue?style=flat&logo=python&logoColor=white)](https://pypi.org/project/FastAPI/0.103.1/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.23.2-blue?style=flat&logo=python&logoColor=white)](https://pypi.org/project/Uvicorn/0.23.2/)
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

4. Запуск FastApi командой
```bash
uvicorn backend.main:app
```
5. Документация по swagger доступна по http://127.0.0.1:8000/docs

### Сделано дополнительно:

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
