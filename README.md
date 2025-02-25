## Структура репозитория

1) **config** - Директория с главными настройками проекта
2) **migrations** - "maddevs_task1/migrations" хранит внутри себя директории с файлами миграций для каждого приложения проекта, текущие директории с миграциями приложений:
    a) **"maddevs_task1/migrations/patients_migrations"** - директория которая хранит все файлы миграций для приложения patients
    b) **"maddevs_task1/migrations/users_migrations"** - директория которая хранит все  файлы миграций для приложения users
3) **src** - директория в которой находится основная логика приложения, она состоит из:
   a) **generals** - директория для утилит, и доп функционала
   b) **patients** - приложение, которое хранит логику пациентов
   c) **users** - приложение, которое хранит логику пользователей
        c.1) **managements/commands** - директория в которой хранится кастомная команда для создания админа
4) **tests** - Директория предназначенная для тестов, тесты проводятся на двух уровнях:
    **API** - тесты работоспособности эндпоинтов
    **моделей** - тесты работоспособности моделей, и их методов.
    **Так-же используются "Фабрики" для создания пользоавтелей, докторов**
5) **docker** - директория, которая содержит файлы конфигурации docker (Dockerfile, entrypoint.sh). docker-compose.yml находится в корневой директории проекта
6) **fixtures** - директория в которой хранятся фикстуры для заполнения таблицы пациентов

## Инструкция по локальному запуску
1) **git clone <https-link>** - склонируйте проект
2) **touch .env .env.db** - в корневой директории создайте файл .env и .env.db для переменных окружения, и заполните их в соответствии с .env.example и .env.db.example
3) **createdb maddevs_task1** - создайте базу данных для проекта (В случае запуска проекта локально, не через докер)
4) **docker-compose up --build** - запустите cборку контейнеров
