from app import app, db
from app.models.tables import User
from app.models.forms import LoginForm, RegisterForm
from flask import render_template, flash, redirect, url_for, session
from flask_login import login_user, current_user


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
                    solved='')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    errors = []
    form = LoginForm()
    if form.validate_on_submit():
        email = User.query.filter_by(email=form.email.data).first()
        if email and email.password == form.password.data:
            login_user(email)
            flash("Logged in.")
            return redirect(url_for("dashboard"))
        else:
            errors.append("Your email or password is incorrect")
    return render_template('login.html',
                           form=form, errors=errors)
