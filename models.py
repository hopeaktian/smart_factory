# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

#数据模型部分

class User(db.Model):
    __tablename__ = 'User'  #表名字默认是类名字的小写版本(如果没有此语句)

    Id = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(255))
    Password = db.Column(db.String(255))
    Gender = db.Column(db.Integer())
    Email = db.Column(db.String(255))
    Tel_Number = db.Column(db.String(255))
    Register_Date = db.Column(db.DateTime, default=datetime.datetime.now)

    # Orders = db.relationship(
    #     'Order',
    #     backref='User',
    #     lazy='dynamic'
    # )

    # Get_Orders = db.relationship(
    #     'Got_Order',
    #     backref='User',
    #     lazy='dynamic'
    # )

    #以下的两个def 可以不用写，系统会自动添加
    def __init__(self, username, password, gender, email, tel):
        self.Username = username
        self.Password = password
        self.Gender = gender
        self.Email = email
        self.Tel_Number = tel

        # def __repr__(self):
        #     return "<User '{} {} {} {} {} {} '>" .format(self.Username, self.Password, self.Gender, self.Email, self.Tel_Number, self.Register_Date)



class Order(db.Model):
    __tablename__ = 'Order'

    Id = db.Column(db.Integer(), primary_key=True)
    Title = db.Column(db.String(255), nullable=False)
    Details = db.Column(db.String(255), nullable=False)
    # Order_Tel = db.Column(db.String(255))
    Finish = db.Column(db.Integer(), nullable=False)

    Order_Date = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    Dead_Date = db.Column(db.DateTime, nullable=False)
    Picture_Name = db.Column(db.String(255))
    User_id = db.Column(db.Integer(), db.ForeignKey('User.Id'), nullable=False)         # 发单用户的Id
    Got_id = db.Column(db.Integer(), db.ForeignKey('User.Id'))                          # 接单用户的Id

    User = db.relationship('User', foreign_keys='Order.User_id')
    Got_User = db.relationship('User', foreign_keys='Order.Got_id')

    Got_Date = db.Column(db.DateTime)                                                     # 接单的时间

    # Get_Orders = db.relationship(
    #     'Got_Order',
    #     backref='Order',
    #     lazy='dynamic'
    # )

    def __init__(self, title):
        self.Title = title

# class Got_Order(db.Model):
#
#     __tablename__ = 'Got_Order'
#
#     Id = db.Column(db.Integer(), primary_key=True)
#     Got_Date = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
#     User_id = db.Column(db.Integer(), db.ForeignKey('User.Id'))
#     Order_id = db.Column(db.Integer(), db.ForeignKey('Order.Id'))
#
#     def __int__(self, order_id):
#         self.Order_id = order_id




class Criticism(db.Model):
    __tablename__ = 'Criticism'

    Id = db.Column(db.Integer(), primary_key=True)
    Nickname = db.Column(db.String(255))
    Criticism = db.Column(db.String(255))
    Cri_Date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, nickname, criticism,):
        self.Nickname = nickname
        self.Criticism = criticism
        #
        # def __repr__(self):
        #     return "< '{} {}' >" .format(self.Nickname, self.Criticism)
