from app import app, db, blueprint
from flask import redirect, url_for, session
from flask_login import login_user
from app.models.tables import User
from sqlalchemy.orm.exc import NoResultFound
from flask_dance.contrib.github import github
from flask_dance.consumer import oauth_authorized

app.register_blueprint(blueprint, url_prefix='/authorized')

@app.route('/auth')
def authenticate():
    if not github.authorized:
        return redirect(url_for('github.login'))
    auth = github.get('/user')
    auth_json = auth.json()
    return 'congrats'

@oauth_authorized.connect_via(blueprint)
def authenticate(blueprint, token):
    auth = blueprint.session.get('/user')
    if auth.ok:
        auth_json = auth.json()
        username = auth_json['login']
        email = auth_json['email']

        query = User.query.filter_by(username=username)
        try:
            user = query.one()
        except NoResultFound:
            user = User(username=username, email=email, solved='')
            db.session.add(user)
            db.session.commit()
        login_user(user)
