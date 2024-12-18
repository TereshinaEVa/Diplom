from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from .forms import UserRegister
from .models import *
from django.http import HttpResponse


def menu_str(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'welcome.html', context)

def registration_page(request):
    info = {}
    person = Persons.objects.all()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            login = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            grade = form.cleaned_data['grade']

            if login in str(person):
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Persons.objects.create(name=login, grade=grade, age=age, password=hash(password))
                info['message'] = f'Приветствуем, {UserRegister.username}!'
    else:
        form = UserRegister()
        info['message'] = form
    return render(request, 'registration_page.html', info)


def welcome_str(request):
    person = Persons.objects.all()
    info = {}
    if request.method == 'POST':
        login = request.POST.get('username')
        password = request.POST.get('password')
        #repeat_password = request.POST.get('repeat_password')

        if login not in str(person) or password not in str(person):
            info['error'] = 'Не верно введены учетные данные. Или пользователь не зарегистрирован.'
        
        else:
            #template = 'personal_str.html'
            #info['message'] = f'Приветствуем, {login}!'
            return render(request, 'menu.html', info)
            
    return render(request, 'registration_page.html', info)

'''def games_menu(request):
    title = 'Магазин'
    games_ = Game.objects.all()
    context = {
        'title': title,
        'games_': games_,
        #'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    }
    return render(request, 'fourth_task/games.html', context)

def cart_str(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'fourth_task/cart.html', context)
    '''
