#!/usr/bin/env python
#coding:utf-8

from os import path
from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for
import datetime, os, time
from sqlalchemy.sql.expression import not_, or_
from app.models import User, Mession

index_blueprint = Blueprint(
    'index',
    __name__,
    template_folder=path.join(path.pardir, 'templates', 'index')
)

def index():
    pass
