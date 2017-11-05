from flask import render_template, flash, redirect, url_for, session
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm

from app.models.tables import User, Challenges
from app.models.forms import FlagForm
import datetime
from notifications import *

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    users = User.query.filter_by(username=current_user.username).first()
    if not current_user.is_authenticated:
        # if user is logged in we get out of here
        return redirect(url_for('login'))
    form = FlagForm()
    if form.validate_on_submit():
        chall = Challenges.query.filter_by(flag=form.flag.data).first()
        if not chall:
            flash('chegou nem perto!')
            return redirect(url_for('dashboard'))
        if chall.flag == form.flag.data:
            user = User.query.filter_by(username=current_user.username).first()
            if str(chall.id) in user.solved:
                flash('já respondeu, só bypassando')
                return render_template('dashboard/index.html', form=form)
            user.score = str(int(user.score) + int(chall.score))
            user.solved = user.solved + ', ' + str(chall.id)
            user.lastSubmit = datetime.datetime.utcnow()
            db.session.commit()
            flash('Acertou, mizeravi')
            return redirect(url_for('dashboard'))
    return render_template('dashboard/index.html', form=form, users=users)
