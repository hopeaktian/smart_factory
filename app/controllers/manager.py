#!/usr/bin/env python
#coding:utf-8
from os import path
from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for, g
import datetime, os, time
from sqlalchemy.sql.expression import not_, or_
from app.models import User, Mession

manager = Blueprint(
    'manager',
    __name__,
    template_folder=path.join(path.pardir, 'templates', 'manager')
)

@manager.before_request
def check_manager():
    if g.current_user == None:
        return render_template('error.html')
    else:
        user = User.query.filter(User.Id == g.current_user.Id, User.Id < 10).first()
        if g.current_user == None or not user :
            return render_template('error.html')

@manager.route('/manager/<int:id>', methods=['GET'])
def Manager(id):
    if g.current_user == None or g.current_user.Id != id:
        return render_template('error.html')
    else:
        return render_template('manager_home.html')

@manager.route('/manager/<int:id>/new_mession', methods=['GET', 'POST'])
def new_mession(id):
    return render_template('new_mession.html')







