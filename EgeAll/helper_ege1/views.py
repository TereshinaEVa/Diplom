from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from .forms import UserRegister, UserWelcome
from .models import *
from django.http import HttpResponse


def menu_str(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'menu.html', context)


def task_list(request):
    title = 'Выбор типа задания'
    tasks_ = Text_and_video.objects.all()
    context = {
        'title': title,
        'tasks_': tasks_,
    }
    return render(request, 'catalog.html', context)


def registration_page(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            login = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            grade = form.cleaned_data['grade']

            if Persons.objects.filter(name=login).exists():
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            else:
                #hashed_password = make_password(password)
                Persons.objects.create(name=login, grade=grade, age=age, password=password)
                info['message'] = f'Приветствуем, {login}!'
                return render(request, 'catalog.html', context=info)
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'registration_page.html', info)


def welcome_str(request):
    info = {}
    if request.method == 'POST':
        login = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Persons.objects.get(name=login)
        except Persons.DoesNotExist:
            info['error'] = 'Пользователь не зарегистрирован.'
            return render(request, 'registration_page.html', info)

        if password != user.password:
            info['error'] = 'Неверный пароль.'
            return render(request, 'welcome.html', info)

        info['message'] = f'Приветствуем, {login}!'
        return render(request, 'catalog.html', info)

    return render(request, 'welcome.html', info)