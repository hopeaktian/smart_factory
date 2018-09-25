# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for
from config import DevConfig
from models import db
from controllers.index import index_blueprint

app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

@app.route('/')
def index():
    return redirect(url_for('index.index'))

app.register_blueprint(index_blueprint)

if __name__ == '__main__':
    app.run('localhost', 80)