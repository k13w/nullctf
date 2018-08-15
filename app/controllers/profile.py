from app import app
from app.models.tables import User
from flask import render_template, redirect, url_for
from flask_login import login_required, logout_user, current_user
from app.models.tables import User, Challenges

@app.route('/profile')
@login_required
def profile():
    users = User.query.filter_by(username=current_user.username).first()
    chall = Challenges.query.all()
    if not current_user.is_authenticated:
        # if user is logged in we get out of here
        return redirect(url_for('login'))
    chall = Challenges.query.all()
    return render_template('dashboard/profile.html', users=users, chall=chall)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
