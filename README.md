# File Storage MVP (Refactored)

Тестовое задание на позицию **Fullstack разработчика (Python + React)**.

Проект представляет собой MVP файлообменника с возможностью:

* загрузки файлов
* асинхронной обработки
* проверки на подозрительный контент
* генерации алертов

## Что было сделано

### Backend

* Проведён рефакторинг архитектуры:

  * разделение на слои: `api`, `domain`, `infrastructure`, `core`
  * внедрён Dependency Injection (`Depends`)
  * выделены репозитории и domain-сервисы
* Переработана асинхронная обработка файлов (Celery)
* Исправлены баги и улучшена работа с БД
* Добавлена пагинация:

  * `GET /files`
  * `GET /alerts`


### Frontend

* Проведён рефакторинг с применением **Feature-Sliced Design**
* Логика разделена на:

  * `entities`
  * `features`
  * `widgets`
  * `shared`
* Вынесена бизнес-логика в кастомные хуки
* Добавлена пагинация (синхронизация с backend)

### Тесты

* Добавлены базовые тесты:

  * API (загрузка файлов, получение списка)
  * domain-слой (FilesDomainService)
* Использован минималистичный подход без сторонних тестовых библиотек


## Архитектура

### Backend

```
src/
 ├── api/              # HTTP слой (FastAPI)
 ├── domain/           # бизнес-логика
 ├── infrastructure/   # БД, Celery, репозитории
 ├── core/             # конфигурация
```

---

### Frontend

```
src/
 ├── entities/
 ├── features/
 ├── widgets/
 ├── shared/
```

## Запуск проекта

```bash
docker compose -f docker-compose.dev.yml up
```

Применить миграции:

```bash
docker exec -it backend alembic upgrade head
```

## Доступ

* Frontend: http://localhost:3000/test
* Backend (Swagger): http://localhost:8000/docs

## Основные эндпоинты

### Файлы

* `GET /files?skip=0&max=10`
* `POST /files`
* `GET /files/{id}`
* `PATCH /files/{id}`
* `DELETE /files/{id}`
* `GET /files/{id}/download`

### Алерты

* `GET /alerts?skip=0&max=10`

## Пагинация

Реализована через параметры:

```http
GET /files?skip=0&max=10
```

* `skip` — смещение
* `max` — количество элементов

## Особенности реализации

* Асинхронный стек (FastAPI + SQLAlchemy async)
* Celery для фоновых задач
* Разделение бизнес-логики и инфраструктуры
* Готовность к масштабированию и тестированию

## Возможные улучшения

* Сделать тесты через pytest и правильно мокать bd
* Расширить обработку файлов (антивирус, content parsing)
* Добавить полноценное логирование и мониторинг
* Добавить alert пользователем

---

Тестовое задание выполнено в рамках демонстрации навыков:

* проектирования архитектуры
* рефакторинга
* работы с асинхронным стеком
* разделения frontend логики
