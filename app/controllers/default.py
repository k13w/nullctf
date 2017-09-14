from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from sqlalchemy import desc

from app.models.tables import User, Challenges
from app.models.forms import LoginForm, RegisterForm

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
		            username=form.username.data)
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

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/dashboard")
def dashboard():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    challenges = Challenges.query.all()
    query = db.session.query(Challenges.category.distinct().label("category"))
    categories = [row.category for row in query.all()]
    ranking = rank(current_user.username)
    return render_template("dashboard/index.html", challenges=challenges, categories=categories, ranking=ranking)

@app.route("/get_chall", methods=["GET", "POST"])
def get_chall(category, score):
    form = FlagForm()
    chall = Challenges.query.filter_by(flag=form.flag.data).all
    if chall and chall.flag == form.flag.data:
        return list(chall)[0]
