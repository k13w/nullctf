from app import app
from app.models.tables import User
from flask import render_template, redirect, url_for
from flask_login import login_required, logout_user

@app.route('/profile')
@login_required
def profile():
    users = User.query.filter(User.username!='').order_by(User.score).all()
    return render_template('dashboard/profile.html', users=users)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
