from flask import render_template, flash, redirect, url_for, session
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from sqlalchemy import desc, asc

from app.models.tables import User, Challenges
from app.models.forms import LoginForm, RegisterForm, FlagForm
import datetime

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash('Username already exists.')
            return redirect(url_for('register'))
        user = User(email=form.email.data,
                    password=form.password.data,
		            username=form.username.data,
                    score='0',
                    solved='')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = User.query.filter_by(email=form.email.data).first()
        if email and email.password == form.password.data:
            login_user(email)
            flash("Logged in.")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid Login!.")
    return render_template('login.html',
                           form=form)

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if not current_user.is_authenticated:
        # if user is logged in we get out of here
        return redirect(url_for('login'))
    form = FlagForm()
    if form.validate_on_submit():
        chall = Challenges.query.filter_by(flag=form.flag.data).first()
        if not chall:
            flash('wrong Flag!')
            return redirect(url_for('dashboard'))
        if chall.flag == form.flag.data:
            user = User.query.filter_by(username=current_user.username).first()
            user.score = str(int(user.score) + int(chall.score))
            user.solved = user.solved + ', ' + str(chall.id)
            user.lastSubmit = datetime.datetime.utcnow()
            db.session.commit()
            flash('Good Job Valid Flag')
            return redirect(url_for('dashboard'))
    return render_template('dashboard/index.html', form=form)


@app.route('/scoreboard')
@login_required
def scoreboard():
    users = User.query.filter(User.username!='admin').order_by(desc(User.score)).all()
    winners = []
    temps = []
    for user in users :
        if rank(user.username) == 1 :
            winners.append(user)
            temps.append(user.lastSubmit)
    winnertime = min(temps)
    return render_template('scoreboard.html', users=users, winnertime=winnertime)

@app.context_processor
def utility_processor():
    def rank(user_name):
        users = User.query.order_by(asc(User.score)).all()
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

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
