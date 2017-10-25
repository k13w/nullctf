from flask import render_template, flash, redirect, url_for, session
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from sqlalchemy import desc

from app.models.tables import User, Challenges
from app.models.forms import LoginForm, RegisterForm, FlagForm

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
            db.session.commit()
            flash('Good Job Valid Flag')
            return redirect(url_for('dashboard'))
    return render_template('dashboard/index.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
