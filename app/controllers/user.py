#!/usr/bin/env python
#coding:utf-8

from os import path
from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for, g
import datetime, os, time
from sqlalchemy.sql.expression import not_, or_
from app.models import User, Mession

user = Blueprint(
    'user',
    __name__,
    template_folder=path.join(path.pardir, 'templates', 'user')
)

@user.route('/register', methods=['GET', 'POST'])
def register():
    global exist
    global flag
    global repassword
    global password_lenth
    repassword = 1
    password_lenth = 1
    exist = 0
    flag = 0
    if request.method == 'POST':
        new_username = request.form.get("Name")

        if User.query.filter_by(Name=new_username).all():
            exist = 1
            # flash(u"注册失败！！用户名已存在!   换个更个性的用户名吧 -_-", category="danger")
        elif request.form.get("Password") != request.form.get("repassword"):
            repassword = 0
            return render_template('register.html', exist=exist, flag=flag, title=u"注册", repassword=repassword)
        elif len(request.form.get("Password")) < 6:

            password_lenth = 0
            return render_template('register.html', exist=exist, flag=flag, title=u"注册", password_lenth=password_lenth)

        else:
            user_forsql = User()
            user_forsql.Password = request.form.get("Password")
            user_forsql.Name = request.form.get("Name")
            user_forsql.Gender = request.form.get("Gender")
            user_forsql.Birth = request.form.get("Birth")
            user_forsql.Position = request.form.get("Position")
            user_forsql.Email = request.form.get("Email")
            user_forsql.Tel_Number = request.form.get("Tel")


            db.session.add(user_forsql)
            db.session.commit()
            flag = 1
            # flash("恭喜您！注册成功", category="success")
    return render_template('register.html', exist=exist, flag=flag, title=u"注册")

@user.route('/login', methods=['GET', 'POST'])
def login():

    # global log
    # global status
    # log = 0
    # status = 1
    session.permanent = True    #设置sission过期时间开关
    if request.method == 'POST':
        userlogin_name = request.form.get("name_login")
        userlogin_password = request.form.get("password_login")
        positon = request.form.get("position")

        # if User.query.filter(or_(User.Username==userlogin_name, User.Email==userlogin_name)).all() and User.query.filter(User.Password==userlogin_password) :
        # return render_template('index2.html', userlogin_name=userlogin_name)
        # print "Success"
        user = User.query.filter(User.Name == userlogin_name, User.Position == positon, User.Password != None).first()
        if user is not None and user.Password == userlogin_password:
            # status = 1
            # log = 1
            flash(u'登陆成功', category="success")
            session['user_id'] = user.Id

            return redirect(url_for('manager.Manager', id=user.Id))

        else:
            flash(u'用户名或密码错误！', category="danger")
            # status = 0
            return  render_template('login.html')
    return render_template('login.html', title=u"登陆")



@user.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))