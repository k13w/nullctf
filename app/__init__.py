from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_dance.contrib.github import make_github_blueprint

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = '04uth'

blueprint = make_github_blueprint(
    client_id = '9731e7aa2917cc2a6d04',
    client_secret = 'f55e7049f045d8363b165658b1ab570a0b69d8b3',
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)

from app.controllers import dashboard, auth, scoreboard, profile, add_chall
from app.models import tables, forms
