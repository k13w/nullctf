from app import app, db
from app.models.tables import User, Challenges
from app.models.forms import addChallenge
from flask import render_template, flash, redirect, url_for, session
from flask_login import login_required
from sqlalchemy.orm.exc import NoResultFound

@app.route("/add_chall", methods=["GET", "POST"])
@login_required
def add():
    form = addChallenge()
    if form.validate_on_submit():
        chall = Challenges.query.filter_by(name=form.name.data)
        try:
            chall = chall.one()
        except NoResultFound:
            chall = Challenges(name=form.name.data, 
                               category=form.category.data,
                               content=form.content.data,
                               flag=form.flag.data,
                               value=form.value.data)
            db.session.add(chall)
            db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('dashboard/add.html', form=form)