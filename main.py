# -*- coding: utf-8 -*-
import datetime, os, time
from flask import Flask, render_template, request, flash, session, redirect, url_for
from config import DevConfig
from werkzeug.utils import secure_filename

# from flask_sqlalchemy import SQLAlchemy
# import models
# from sqlalchemy.sql.expression import not_, or_

from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config.from_object(DevConfig)

# db = SQLAlchemy(app)

# 自定义jinja过滤器
def time_format(l):
    return str(l)[:-7]
app.add_template_filter(time_format, 'format_time')


#bootstrap = Bootstrap(app)

# UPLOAD_FOLDER = "./static/Upload_File/"
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS




# 路由部分
def checkuser():
    if 'username' in session:
        global user
        user = User.query.filter_by(Username=session['username']).first()

@app.route('/')
def index():
    if 'username' in session:
        global user
        user = User.query.filter_by(Username=session['username']).first()
        return render_template('index.html', title=u'智慧工厂', userlogin_name=session['username'], user=user)
    return render_template('index.html', title=u"智慧工厂")

# @app.route('/MP_verify_FcIWodemzDz6J6Op.txt')
# def weixin():
#     return render_template('MP_verify_FcIWodemzDz6J6Op.txt')
#
#
# @app.errorhandler(404)
# def page_not_found(e):
#     if 'username' in session:
#         global user
#         user = User.query.filter_by(Username=session['username']).first()
#         return render_template('error.html', title=u"错误", user=user, userlogin_name=session['username']), 404
#     return render_template('error.html', title=u"错误"), 404
#
# @app.errorhandler(500)
# def page_not_found(e):
#     if 'username' in session:
#         global user
#         user = User.query.filter_by(Username=session['username']).first()
#         return render_template('error.html', title=u"错误", user=user), 500
#     return render_template('error.html', title=u"错误"), 500
#
# @app.route('/messagewall', methods=['GET', 'POST'])
# def messagewall():
#     global success
#     global lenth
#     global userlogin_name
#     success = 0             #评论初始值为0即失败
#     lenth = 0
#     allCri = Criticism.query.order_by(Criticism.Id.desc()).all()
#     lenth = len(allCri)
#
#     if 'username' in session:
#         user = User.query.filter_by(Username=session['username']).first()
#         userlogin_name = session['username']
#         if request.method == 'POST':
#             Criticismfrosql = Criticism(request.form.get("nickname"), request.form.get("criticism"))
#             db.session.add(Criticismfrosql)
#             db.session.commit()
#             success = 1
#             allCri = Criticism.query.order_by(Criticism.Id.desc()).all()
#             lenth = len(allCri)
#
#         return render_template('messagewall.html', title=u"留言墙", success=success, allCri=allCri, lenth=lenth, userlogin_name=session['username'], user=user)
#     else:
#         if request.method == 'POST':
#             Criticismfrosql = Criticism(request.form.get("nickname"), request.form.get("criticism"))
#             db.session.add(Criticismfrosql)
#             db.session.commit()
#             success = 1
#             allCri = Criticism.query.order_by(Criticism.Id.desc()).all()
#             lenth = len(allCri)
#
#         return render_template('messagewall.html', title=u"留言墙", success=success, allCri=allCri, lenth=lenth)
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     checkuser()
#     global log
#     global status
#     log = 0
#     status = 1
#     if request.method == 'POST':
#         userlogin_name = request.form.get("name_login")
#         userlogin_password = request.form.get("password_login")
#
#         # if User.query.filter(or_(User.Username==userlogin_name, User.Email==userlogin_name)).all() and User.query.filter(User.Password==userlogin_password) :
#         # return render_template('index2.html', userlogin_name=userlogin_name)
#         # print "Success"
#         user = User.query.filter_by(Username=userlogin_name).first()
#         if user is not None and user.Password==userlogin_password:
#             status = 1
#             log = 1
#             # flash(u'登陆成功', category="success")
#             session['username'] = userlogin_name
#
#             return render_template('index2.html', userlogin_name=session['username'], log=log, title=u"登陆", user=user)
#
#         else:
#             # flash(u'用户名或密码错误！', category="danger")
#             status = 0
#             return  render_template('login2.html', status=status, log=log, title=u"登陆", user=user)
#     return render_template('login2.html', title=u"登陆", log=log)
#
#
# @app.route('/logout', methods=['GET', 'POST'])
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('index'))
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     global exist
#     global flag
#     global repassword
#     global password_lenth
#     repassword = 1
#     password_lenth = 1
#     exist = 0
#     flag = 0
#     if request.method == 'POST':
#         new_username = request.form.get("Name")
#
#         if User.query.filter_by(Username=new_username).all():
#             exist = 1
#             # flash(u"注册失败！！用户名已存在!   换个更个性的用户名吧 -_-", category="danger")
#         elif request.form.get("Password") != request.form.get("repassword"):
#             repassword = 0
#             return render_template('register.html', exist=exist, flag=flag, title=u"注册", repassword=repassword)
#         elif len(request.form.get("Password")) < 6:
#
#             password_lenth = 0
#             return render_template('register.html', exist=exist, flag=flag, title=u"注册", password_lenth=password_lenth)
#
#         else:
#             user_forsql = User(new_username, request.form.get("Password"), request.form.get("Gender"), request.form.get("Email"), request.form.get("Tel"))
#             db.session.add(user_forsql)
#             db.session.commit()
#             flag = 1
#             # flash("恭喜您！注册成功", category="success")
#     return render_template('register.html', exist=exist, flag=flag, title=u"注册")
#
# # 发订单
# @app.route('/order', methods=['GET', 'POST'])
# def order(success=0):
#     checkuser()
#     global now_time
#     now_time = datetime.datetime.now()
#
#
#     if 'username' not in session:
#         return render_template('notlogin.html', title=u"创建订单")
#     elif request.method == 'POST' and not request.files.has_key("inputFile"):
#
#         user_now = User.query.filter_by(Username=session['username']).first()
#         new_order = Order(request.form.get("title"))
#         new_order.Details = request.form.get("detials")
#         new_order.Dead_Date = request.form.get("diedate")
#         new_order.Finish = 0
#         new_order.User_id = user_now.Id
#
#         db.session.add(new_order)
#         db.session.commit()
#         success = 1
#
#         return render_template('order.html', title=u"创建订单", userlogin_name=session['username'], user=user, success=success, now_time=now_time)
#
#     elif request.method == 'POST':
#         user_now = User.query.filter_by(Username=session['username']).first()           # 数据库查询并取得当前用户对象
#         new_order = Order(request.form.get("title"))                                    # 数据库实例化新的Order对象
#
#         new_order.Details = request.form.get("detials")
#         new_order.Dead_Date = request.form.get("diedate")
#         new_order.Finish = 0
#         new_order.User_id = user_now.Id
#
#
#         db.session.add(new_order)
#         db.session.commit()                         # 先将除了图片的信息提交数据库，以免下面图片Id无法获取
#
#         file = request.files['inputFile']
#         filename = file.filename
#         index_point = filename.index(".")
#         filename = str(new_order.Id)+filename[index_point:]
#         basepath = os.path.dirname(__file__)
#         upload_path = os.path.join(basepath, 'static/Upload_File', secure_filename(filename))
#         file.save(upload_path)
#
#         new_order.Picture_Name = filename
#         db.session.add(new_order)
#         db.session.commit()                         # 再将图片信息提交数据库
#
#         success = 1
#
#     return render_template('order.html', title=u"创建订单", userlogin_name=session['username'], user=user, success=success, now_time=now_time)
#
# # 任务大厅展示
# @app.route('/orderwall', methods=['GET', 'POST'])
# def orderwall():
#     # now_time = float(time.mktime(datetime.datetime.now().timetuple()))
#     global datetime
#     datetime = datetime
#
#     checkuser()
#     allorderwall = Order.query.order_by(Order.Id.desc()).all()
#     # user = User.query.all()
#     lenth = Order.query.count()
#
#     if 'username' in session:
#         return render_template('orderwall.html', title=u"任务广场",allorderwall=allorderwall, lenth=lenth, userlogin_name=session['username'], user=user, datetime=datetime)
#     return render_template('orderwall.html', title=u"任务广场",allorderwall=allorderwall, lenth=lenth, datetime=datetime)
#
# @app.route('/join', methods=['GET', 'POST'])
# def join():
#     checkuser()
#     if 'username' in session:
#         return render_template("join.html", title=u"加入我们", user=user)
#     return render_template("join.html", title=u"加入我们")
#
# @app.route('/school_net', methods=['GET', 'POST'])
# def shcool_net():
#     checkuser()
#     if 'username' in session:
#         return render_template("net_tech.html", title=u"校园网共享教程", user=user)
#     return render_template("net_tech.html", title=u"校园网共享教程")
#
#
# # 订单详情
# @app.route('/orderwall/<int:order_id>', methods=['GET', 'POST'])
# def showdetails(order_id):
#     global datetime
#     datetime = datetime
#     checkuser()
#     AboutOrder = Order.query.filter_by(Id=order_id).first()
#     if 'username' in session:
#         return render_template('OrderDetails.html', title=u"任务详情", AboutOrder=AboutOrder, userlogin_name=session['username'], user=user, datetime=datetime)
#     return render_template('OrderDetails.html', title=u"任务详情", AboutOrder=AboutOrder, datetime=datetime)
#
# # 确认接单
# @app.route('/orderwall/<int:order_id>/confirm', methods=['GET', 'POST'])
# def getorder(order_id):
#     checkuser()
#     got_success = 0
#     AboutOrder = Order.query.filter_by(Id=order_id).first()
#     if 'username' not in session:
#         return render_template('notlogin.html', title=u"请先登陆")
#     elif request.method == 'POST':
#         if request.form.get("confirm") == "1":
#             get_user = User.query.filter_by(Username=session['username']).first()
#             AboutOrder.Got_id = get_user.Id
#             AboutOrder.Got_Date = datetime.datetime.now()
#             db.session.add(AboutOrder)
#             db.session.commit()
#             got_success = 1
#             return redirect(url_for('takein', user_id=get_user.Id))
#         else:
#             return redirect(url_for('orderwall'))
#
#     return render_template('confirmorder.html', title=u"确认接单", AboutOrder=AboutOrder, userlogin_name=session['username'], got_success=got_success, user=user)
#
# @app.route('/user/<int:user_id>/sendout', methods=['POST', 'GET'])
# def sendout(user_id):
#     checkuser()
#
#     AboutOrder = Order.query.filter_by(User_id=user_id).order_by(Order.Id.desc()).all()
#     lenth = len(AboutOrder)
#     if request.method == "POST":
#         user_order = Order.query.filter_by(Id=request.form.get("order_id")).first()
#         if request.form.get("cancel") == "1":                                                       #取消订单
#             user_order.Finish = request.form.get("cancel")
#             db.session.add(user_order)
#             db.session.commit()
#         else:
#             user_order.Finish = request.form.get("finish")                                          #确认收货
#             db.session.add(user_order)
#             db.session.commit()
#     return render_template('sendout.html', title=u"发出订单", AboutOrder=AboutOrder, lenth=lenth, userlogin_name=session['username'], user=user)
#
# @app.route('/user/<int:user_id>/takein')
# def takein(user_id):
#     checkuser()
#
#     AboutOrder = Order.query.filter_by(Got_id=user_id).order_by(Order.Id.desc()).all()
#     lenth = len(AboutOrder)
#     return render_template('takein.html', title=u"接受订单", AboutOrder=AboutOrder, lenth=lenth, userlogin_name=session['username'], user=user)


if __name__ == '__main__':
    app.run(host='localhost', port=80)
