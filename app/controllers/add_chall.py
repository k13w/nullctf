from app import app, db
from app.models.tables import User, Challenges
from app.models.forms import addChallenge
from flask import render_template, flash, redirect, url_for, session
from flask_login import login_required

@app.route("/add", methods=["GET", "POST"])
def add():
    form = addChallenge()
    if form.validate_on_submit():
        chall = Challenges.query.filter_by(name=form.name.data).first()
        users = User.query.filter(User.username=='heaven').first
        if chall is not None:
            return redirect(url_for('index'))
        chall = Challenges(name=form.name.data, category=form.category.data,
                           content=form.content.data, flag=form.flag.data,
                           value=form.value.data)
        db.session.add(chall)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('dashboard/add.html', form=form)

@app.route("/add", methods=["GET", "POST"])
def update():
    if request.method == 'POST':
        chal_type = request.form['chaltype']
