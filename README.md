# To‑Do App

## 📝 Вступ  
Один простий веб-додаток для керування списком завдань (To‑Do list). Розроблений з використанням Django, PostgreSQL, Bootstrap, HTML і механізму сесій для автентифікації користувачів.

## 📚 Зміст  
- [Огляд](#️%D0%BE%D0%B3%D0%BB%D1%8F%D0%B4)  
- [Технології](#️%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D1%96%D1%97)  
- [Установка](#️%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0)  
- [Налаштування](#️%D0%BD%D0%B0%D0%BB%D0%B0%D1%88%D1%82%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F)  
- [Запуск програми](#️%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%B8)  
- [Функціональні можливості](#️%D1%84%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96-%D0%BC%D0%BE%D0%B6%D0%BB%D0%B8%D0%B2%D0%BE%D1%81%D1%82%D1%96)  
- [Приклади](#️%D0%BF%D1%80%D0%B8%D0%BA%D0%BB%D0%B0%D0%B4%D0%B8)  
- [Вирішення проблем](#️%D0%B2%D0%B8%D1%80%D1%96%D1%88%D0%B5%D0%BD%D0%BD%D1%8F-%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC)  
- [Контриб’ютори](#️%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%B8%D0%B1%D1%8E%D1%82%D0%BE%D1%80%D0%B8)  
- [Ліцензія](#️%D0%BB%D1%96%D1%86%D0%B5%D0%BD%D0_z)

## Огляд  
Цей додаток дозволяє користувачеві реєструватися (за бажанням) або працювати анонімно за сесією, створювати, переглядати й видаляти завдання. Інтерфейс зроблений у стилі Bootstrap для мобіль-респонсивності.

## Технології  
- **Backend**: Django (Python)  
- **База даних**: PostgreSQL  
- **Шаблони**: HTML + Django Template Language  
- **Сесії**: стандартний сесійний middleware Django  
- **UI**: Bootstrap CSS/JS

## Установка  
1. `git clone https://github.com/Salonaut/to-do-app.git`  
2. Перейти у папку: `cd to-do-app`  
3. Створити віртуальне середовище: `python3 -m venv venv`  
4. Активувати: `source venv/bin/activate` (Linux/Mac) або `.\venv\Scripts\activate` (Windows)  
5. Встановити залежності: `pip install -r requirements.txt`

## Налаштування  
- Створити файл `.env` або оновити `settings.py` (якщо без env):  
  ```ini
    SECRET_KEY='django-insecure-of5774b#4rimp&!mfedxw2=f-5s$=3p1@1rai$vlfxe=y_ln'
    DB_NAME=todo_db_t5as
    DB_USER=todo_user
    DB_PASSWORD=2AL7WgPbhh5018ZQD7rMvQT12hFHgJH3
    DB_HOST=dpg-d235o27diees739avu5g-a.frankfurt-postgres.render.com
    DB_PORT=5432

