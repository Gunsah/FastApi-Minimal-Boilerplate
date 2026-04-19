# FastApi-Minimal-Boilerplate (Docker)

A minimal FastAPI boilerplate for DevOps course

## Что делает проект

Минимальный шаблон на FastAPI с эндпоинтами для расчётов и сохранения состояния. Данные хранятся в директории `/data` и не теряются при перезапуске контейнера.

## Какой вариант выбран и почему

**Вариант 3**. Выбран, так как демонстрирует работу с persistent-данными через named volumes, что является обязательным требованием для production-контейнеризации.

## Как запустить (Вариант 3)

```bash
# Клонировать репозиторий
git clone https://github.com/Gunsah/FastApi-Minimal-Boilerplate
cd FastApi-Minimal-Boilerplate

# Собрать образ
docker build -t my-web .

# Запустить с сохранением данных
docker run -d -p 8080:8080 -v app-data:/data --name app my-web

# Открыть в браузере
http://localhost:8080/docs
```

## Управление контейнером

```bash
# Посмотреть логи
docker logs app

# Остановить и удалить
docker stop app && docker rm app
```

## Проверка сохранности данных

```bash
# Сохранить значение
curl -X POST "http://localhost:8080/state/test?value=hello"

# Прочитать
curl http://localhost:8080/state/test

# Перезапустить контейнер
docker stop app && docker rm app
docker run -d -p 8080:8080 -v app-data:/data --name app my-web

# Данные должны остаться
curl http://localhost:8080/state/test
```
