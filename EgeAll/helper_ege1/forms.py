from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин: ', required=True)
    password = forms.CharField(min_length=8, label='Введите пароль: ', required=True)
    repeat_password = forms.CharField(max_length=30, label='Повторите пароль: ', required=True)
    age = forms.CharField(max_length=3, label='Введите свой возраст: ', required=True)
    grade = forms.CharField(max_length=3, label='Введите класс: ', required=True)

class UserWelcome(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин: ', required=True)
    password = forms.CharField(min_length=8, label='Введите пароль: ', required=True)
