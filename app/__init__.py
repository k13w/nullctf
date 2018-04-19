from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_dance.contrib.github import make_github_blueprint
from configparser import ConfigParser

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = '04uth'

cp = ConfigParser()
cp.read_file(open('api.ini'))

blueprint = make_github_blueprint(
    client_id = cp['API']['client_id'],
    client_secret = cp['API']['client_secret'],
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)

from app.controllers import dashboard, auth, scoreboard, profile, add_chall
from app.models import tables, forms
