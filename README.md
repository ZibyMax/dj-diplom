# Дипломный проект по курсу «Django: создание функциональных веб-приложений»

## Описание проекта

Сайт интернет магазина.
Реализовано:
1. Интерфейс администратора с возможностью редактирования товаров, разделов и статей для главной страницы
2. Авторизация с использованием элетронной почты вместо логина
3. Главное меню с возможностью группировки разделов по категориям товаров
4. Страницы со списком товаров выюранной категории
5. Страницы с описанием конкретного товара
6. Возможность добавления товаров в корзину. При добавлении товара ведется подсчет количества выбранных товаров.
7. Корзина со списком выбранных товаров. При выполненной авторизации содержимое может быть оформлено в виде заказа.
8. Страница с детализированным списком заказов авторизованного пользователя.


## Инструкция по установке

1. Установите зависимости:
pip install -r requirements.txt

2. Выполните миграции:
manage.py migrate

3. Загрузите тестовые данные в базу:
manage.py loaddata db.json

4. Запустите тестовый сервер
manage.py runserver

Тестовый суперпользователь:
логин: admin
пароль: admin
почта: admin@admin.admin