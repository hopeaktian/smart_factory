# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, render_template, session, g
from config import DevConfig
# from models import db
from app.models import User, db
from controllers.user import user
import datetime

app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

app.permanent_session_lifetime = datetime.timedelta(seconds=5*60)          #设置sission过期时间为5min


@app.route('/')
def index():
    return render_template('index.html')

@app.before_request
def check_user():
    if 'user_id' in session:
        g.current_user = User.query.filter_by(Id=session['user_id']).one()
        print g.current_user

    else:
        g.current_user = None



app.register_blueprint(user)

if __name__ == '__main__':
    app.run('localhost', 80)