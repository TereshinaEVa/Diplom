from flask import Flask, render_template, url_for, request, flash, session, redirect

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
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Ok')
            #print(request.form['username'])
        else:
            flash('Not found')

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