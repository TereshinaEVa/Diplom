# Diplom
# Анализ и сравнение написания web-приложений с использованием разных фреймворков
## Разработка простого веб-приложения с использованием Django, Flask и FastAPI 
## Особенности создания приложения в Django
### Установить Django в активную среду
```
pip install Django
```
## Создание проекта
Чтобы начать работу, мы создадим новый проект и базу данных, а затем запустим веб-сервер. Во всех примерах ниже проект будет называться **EgeAll**
```
django-admin startproject EgeAll
```
## Создать новое приложение
Проект Django состоит из одного или нескольких приложений.
```
python manage.py startapp
```
После выполнения этой команды вы можете просмотреть проект по адресу http://localhost:8000/.
```
python manage.py runserver
```

## Работа с моделями
Данные в проекте Django представлены в виде набора моделей — объектов Python, определяющих структуру хранения этих данных.

Определение модели
Чтобы определить модель для вашего приложения, измените файл models.py, созданный в папке приложения. 
Метод __str __() сообщает Python, как отображать экземпляр модели в строковом представлении. Django использует этот механизм для отображения объектов в формах.
```
from django.db import models

class Persons(models.Model):

    name = models.CharField(max_length=50)  # username аккаунта
    grade = models.CharField(max_length=20)
    age = models.IntegerField()
    password = models.CharField(max_length=20, default='12345678')

    def __str__(self):
        return self.name
```
Теперь открываем файл view.py. Здесь располагаются функции представления, которые обеспечивают функционирование логики приложения. В файле уже есть одна строка from django.shortcuts import render. Добавим обработку https запросов и функции представления для страниц проекта. В итоге содержимое может выглядеть так:
```
def task_list(request):
    title = 'Выбор типа задания'
    tasks_ = Text_and_video.objects.all()
    context = {
        'title': title,
        'tasks_': tasks_,
    }
    return render(request, 'catalog.html', context)
```
Теперь создадим файл urls.py, чтобы приложение могло сопоставить маршруты и страницы.
```
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from helper_ege1.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', registration_page),
    path('sing_in/', welcome_str),
    path('catalog/', task_list),
    path('menu/', menu_str),
]
```
Главное - не забыть импортировать используемые нужные части проекта друг в друга.

Далее, возможно подключить и оформить панень администратора в файле admin.py
Например:
```
@admin.register(Text_and_video)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'original_text_url', 'original_video_url')
    list_filter = ('title', )
    list_per_page = 20
```
Здесь мы задаем то, как будет вести себя панель администрирования, каким образом ы сможем вносить данные и как обращаться к ним.

### Особенности создания приложения в FastAPI
##Первый шаг — установка FastAPI.
```
pip install fastapi[all]
```
[all] - обязательно, чтобы установились все необходимые библиотеки.

в том числе и uvicorn, который может быть использован как сервер для запуска кода.
```
python uvicorn main:app  
```
(в некоторых случаях python3 uvicorn main:app) Для того, чтобы ьфшт сработал, нужно находиться в папке проекта.

В файле указывается вся необходимая для запуска приложения информация.
```
from fastapi import FastAPI
from app.routers import user as ur
from app.routers import task as tr

app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True})


@app.get('/')
async def welcome():
    return {"message": "Welcome to the materials for solving tasks for the EGE  in computer science"}

app.include_router(tr.router)
app.include_router(ur.router)
```

Также в файле schemas.py создаются основные схемы для данных, которые будут храниться в проекте.


Далее, в папке routers создаются файлы, которые будут описывать поведение сртаниц и их адреса.

Адрес указывается в декораторе в скобках. Также, декоратор указывает на тип операции: 
@app.get() - запрос
@app.post() - создание данных
@app.put() - изменение данных
@app.delete() - удаление данных

Пример:
```
@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks
```
Далее создаются модели для будущих баз данных. Благодаря SQLAlchemy создание баз данных происходит проще, чем при создании напрямую через sqlaite3.
![image](https://github.com/user-attachments/assets/2213cd3d-acf7-4df9-afbb-99d58fb43d12)
Создается папка backand и в ней создаются файлы, которые будут "следить" за создание нашей будущей базы.
Далее, cоздаем базу данных и таблицы. Для этого нужно выполнить команду alembic init alembic. Она создаст директорию Alembic с необходимыми файлами конфигурации

Сгенерировать миграцию. Для этого нужно выполнить команду 
```
alembic revision --autogenerate -m "Create users table"
```
При этом создается папка миграции и создается файл миграции, который хранит информацию о структуре базы данных.
Для внесения изменений в структуру, необходимо выполнить миграцию (файлы миграции перезапишутся и в конечном файле БД изменится)
```
alembic upgrade
```
Остальная работа с данными может осуществяться через удобную панель управления сайтом (документация)
### Особенности создания приложения в Flask
