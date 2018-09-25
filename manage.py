# -*- coding: utf-8 -*-
from flask_script import Manager, Server
from app import app
from app.models import db, User, Mession

from flask_sqlalchemy import SQLAlchemy
manager = Manager(app)
manager.add_command("server", Server())

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Mession=Mession)

if __name__ == "__main__":
    manager.run()
