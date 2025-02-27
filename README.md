# To-Do List API (Django REST Framework)

## 📌 Описание проекта
To-Do List API — это веб-приложение для управления задачами. Оно включает систему аутентификации JWT, API для работы с задачами, тегами и комментариями, а также поддержку фоновых задач с Celery и документацию Swagger.

## 🚀 Технологии
- **Python 3.13**
- **Django 5.1.6**
- **Django REST Framework**
- **DRF SimpleJWT** (JWT-аутентификация)
- **drf-yasg** (Swagger-документация)
- **Celery + Redis** (Фоновые задачи)

---

## 🔧 Установка и запуск проекта

### 1️⃣ Клонирование репозитория
```bash
git clone https://github.com/ТВОЙ_GITHUB/РЕПОЗИТОРИЙ.git
cd РЕПОЗИТОРИЙ
```

### 2️⃣ Создание виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # для macOS/Linux
venv\Scripts\activate  # для Windows
```

### 3️⃣ Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4️⃣ Применение миграций
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Создание суперпользователя (для входа в админку)
```bash
python manage.py createsuperuser
```

### 6️⃣ Запуск сервера
```bash
python manage.py runserver
```

Теперь API доступен по адресу: **http://127.0.0.1:8000/**

---

## 🔑 Аутентификация (JWT)

### 1️⃣ Получение токена
Отправьте **POST**-запрос на `/api/token/` с данными пользователя:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
Ответ:
```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

### 2️⃣ Обновление токена
POST-запрос на `/api/token/refresh/`:
```json
{
    "refresh": "your_refresh_token"
}
```
Ответ:
```json
{
    "access": "your_new_access_token"
}
```

### 3️⃣ Использование токена
Добавьте `Authorization: Bearer your_access_token` в заголовки запросов.

---

## 📝 API Эндпоинты

### 🔹 Задачи (Tasks)
- **GET /todolist/tasks/** — Получить список задач
- **POST /todolist/tasks/** — Создать задачу
- **GET /todolist/tasks/{id}/** — Получить конкретную задачу
- **PUT /todolist/tasks/{id}/** — Обновить задачу
- **DELETE /todolist/tasks/{id}/** — Удалить задачу

### 🔹 Теги (Tags)
- **GET /todolist/tags/** — Получить список тегов
- **POST /todolist/tags/** — Создать тег

### 🔹 Комментарии (Comments)
- **GET /todolist/comments/** — Получить комментарии
- **POST /todolist/comments/** — Добавить комментарий

---

## 📜 Документация Swagger
Документация API доступна по адресу:
- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

---

## ⏳ Настройка Celery (Фоновые задачи)

### 1️⃣ Запуск Redis (если не установлен, установите)
```bash
redis-server
```

### 2️⃣ Запуск Celery
```bash
celery -A myproject worker --loglevel=info
```


