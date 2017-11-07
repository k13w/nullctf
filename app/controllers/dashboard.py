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
    errors = []
    users = User.query.filter_by(username=current_user.username).first()
    chall = Challenges.query.all()
    if not current_user.is_authenticated:
        # if user is logged in we get out of here
        return redirect(url_for('login'))
    form = FlagForm()
    chall = Challenges.query.all()
    if form.validate_on_submit():
        chall1 = Challenges.query.filter_by(flag=form.flag.data).first()
        if not chall1:
<<<<<<< HEAD
            flash(FLAG_INCORRECT)
=======
            flash(FLAG_INCORRET)
>>>>>>> 1cd61961236e1276789d3ec97bbc5a40004a6ef3
            return redirect(url_for('dashboard'))
        if chall1.flag == form.flag.data:
            user = User.query.filter_by(username=current_user.username).first()
            if str(chall1.id) in user.solved:
                flash(FLAG_SUBMITTED_ALREADY)
                print(chall)
                return render_template('dashboard/index.html', form=form, users=users, chall=chall)
            user.score = str(int(user.score) + int(chall1.value))
            user.solved = user.solved + str(chall1.id) + ', '
            user.lastSubmit = datetime.datetime.utcnow()
            db.session.commit()
            flash(FLAG_SUCCESS)
            return redirect(url_for('dashboard'))
    return render_template('dashboard/index.html', form=form, users=users, chall=chall )
