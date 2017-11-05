#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app import app
from app.models.tables import User
from flask import render_template, redirect, url_for
from flask_login import login_required
from sqlalchemy import desc

@app.route('/scoreboard')
@login_required
def scoreboard():
    users = User.query.filter(User.username!='').order_by(desc(User.score)).all()
    winners = []
    temps = []
    for user in users :
        print(temps)
        if rank(user.username) == 1 :
            winners.append(user)
            temps.append(user.lastSubmit)
    return render_template('scoreboard.html', users=users)

@app.context_processor
def utility_processor():
    def rank(user_name):
        users = User.query.order_by(desc(User.score)).all()
        myuser = User.query.filter_by(username=user_name).first()
        l = []
        for user in users :
            l.append(user.score)
        return int(l.index(myuser.score)) + 1
    return dict(rank=rank)

def rank(user_name):
    users = User.query.order_by(desc(User.score)).all()
    myuser = User.query.filter_by(username=user_name).first()
    l = []
    for user in users :
        l.append(user.score)
    return int(l.index(myuser.score)) + 1
