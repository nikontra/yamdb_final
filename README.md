# api_yamdb
## **Описание проекта**
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «книги», «фильмы», «музыка». Список категорий расширяется командой.
Проект «YaMDb» реализован на Django, в свою очередь «API для YaMDb» реализован с использованием библиотеки Django REST Framework (DRF).
DRF мощный и гибкий инструмент для построения Web API, который имеет следующие преимущества:
* Крайне удобная для разработчиков браузерная версия API;
* Наличие пакетов для OAuth1a и OAuth2 авторизации;
* Сериализация, поддерживающая ORM и не-ORM источники данных;
* Возможность полной и детальной настройки - можно использовать обычные представления-функции, если вы не нуждаетесь в мощном функционале;
* Расширенная документация и отличная поддержка сообщества.<br/>

Через API Yatube можно публиковать отзывы и делиться своим мнением в комментариях.

## **Шаблон наполнения env-файла**
```
DB_ENGINE= # указываем базу данных, с которой работаем
DB_NAME= # имя базы данных
POSTGRES_USER= # логин для подключения к базе данных
POSTGRES_PASSWORD= # пароль для подключения к БД
DB_HOST= # название сервиса (контейнера)
DB_PORT= # порт для подключения к БД 
```

## **Как запустить проект**

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/nikontra/infra_sp2.git

```
```
cd api_yamdb
```
Для сборки и запуска контейнеров использовать команду:
```
sudo docker-compose up
```
Если необходимо запустить контейнеры в "фоновом режиме":
```
sudo docker-compose up -d
```
Для пересборки контейнеров и запуска в "фоновом режиме":
```
sudo docker-compose up -d --build
```
После запуска контейнеров,  чтобы создать миграций, суперпользователя и собрать статику, необходимо последовательно выполнить команды:
```
sudo docker-compose exec web python manage.py migrate 
sudo docker-compose exec web python manage.py createsuperuser
sudo docker-compose exec web python manage.py collectstatic --no-input
```
Для остановки контейнеров нажать CTRL+C.
Если контейнеры запущены в "фоновом режиме":
```
sudo docker-compose stop
```
Для остановки и удаления контейнеров:
```
sudo docker-compose down -v
```

## **Заполнение базы данных**
Скопировать файл с данными для базы fixtures.json в контейнер infra_web:
```
sudo docker cp fixtures.json CONTAINER_ID:/app
```
ID контейнера можно узнать выполнив команду:
```
sudo docker container ls -a
```
Для заполнения базы данными выполнить команду:
```
sudo docker-compose exec web python manage.py loaddata fixtures.json
```
База данных заполнена.

## **Информация об авторе**
Автор проекта: Третьяков Николай
Контакты: 
 - Email: nikontra@yandex.ru
 - Git: https://github.co

![example workflow](https://github.com/nikontra/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
