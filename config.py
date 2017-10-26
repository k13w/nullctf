import os.path
from app import app
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True