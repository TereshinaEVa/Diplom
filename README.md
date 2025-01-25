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

![image](https://github.com/user-attachments/assets/e7bde48e-606d-47a3-b95b-74c7bd572452)

### Особенности создания приложения в Flask
