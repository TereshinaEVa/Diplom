import sqlite3
from sqlite3 import *
import os
from flask import Flask, render_template, request, g

DATABASE = '/tmp/forege.db'
DEBAG =True
SECRET_KEY = 'gjhbjb4ug8744w8374gfbsi123'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'forege.db')))

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def getUsers(self):
        users_ = '''SELECT * FROM users'''
        try:
            self.__cur.execute(users_)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('Ошибка чтения из БД')
        return []

    def addPost(self, username, password, ege, grade):
        try:
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?,?,?,?)", (username, password, ege, grade))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка регистрации пользователя' + str(e))
            return False
        return True


def connect_db():
    conn = connect(app.config['DATABASE'])
    conn.row_factory = Row
    return conn

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'users_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/reg')
def registrations():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('registration_page.html')

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'users_db'):
        g.link_db.close()

# if __name__ == '__main__':
#     app.run(debug=True)