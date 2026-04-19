## Как запустить (Вариант 3)

```bash
# Клонировать репозиторий
git clone <ссылка_на_твой_репо>
cd FastApi-Minimal-Boilerplate

# Собрать образ
docker build -t my-web .

# Запустить с сохранением данных
docker run -d -p 8080:8080 -v app-data:/data --name app my-web

# Открыть в браузере
# → http://localhost:8080/docs