import sqlite3
import os
from flask import Flask, request, g

DATABASE = '/tmp/forege.db'
DEBUG = True
SECRET_KEY = 'gjhbjb4ug8744w8374gfbsi123'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'forege.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'users_db1'):
        g.users_db1 = connect_db()
    return g.users_db1


# @app.route('/reg')
# def registrations():
#     db = get_db()
#     dbase = FDataBase(db)
#     return render_template('registration_page.html')

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'users_db1'):
        g.users_db1.close()

create_db()


# if __name__ == '__main__':
#     app.run(debug=True)