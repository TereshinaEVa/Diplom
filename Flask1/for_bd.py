from sqlite3 import *
import os
from flask import Flask, render_template, request, g

DATABASE = '/tmp/forege.db'
DEBAG =True
SECRET_KEY = 'gjhbjb4ug8744w8374gfbsi123'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'forege.db')))

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
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/')
def index():
    db = get_db()
    return render_template('menu.html')

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()
