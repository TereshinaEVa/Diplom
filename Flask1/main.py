from flask import Flask, render_template, url_for, request, flash, session, redirect
from users_db import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gjhbjb4ug8744w8374gfbsi'

@app.route('/')
def menu():
    # url_for('menu')
    return render_template('menu.html', title='Главная страница')


@app.route('/catalog')
def catalog():
    # url_str=url_for('catalog')
    return render_template('catalog.html', title='Полезные материалы')


@app.route('/reg', methods=['POST', 'GET'])
def registration():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        if request.form['username'] in dbase:
            flash('Пользователь уже существует')
        elif request.form['password'] != request.form['repeat_password']:
            flash('Пароли не совпадают')
            #print(request.form['username'])
        else:
            res = dbase.addPost(request.form['username'],
                                request.form['password'],
                                request.form['age'],
                                request.form['grade']
                                )
            return redirect(url_for('welcome'))
    return redirect(url_for('registration'))

@app.route('/welcome', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and request.form['username'] == 'Eva'\
            and request.form['password'] == '12345678':
        return redirect(url_for('menu'))
    else:
        flash('Ошибка в логине или пароле')

    return render_template('welcome.html', title='Авторизация')



if __name__ == '__main__':
    app.run(debug=True)