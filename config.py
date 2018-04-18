import os.path
from app import app
basedir = os.path.abspath(os.path.dirname(__file__))

ctf_name = "HCTF"
DEBUG = True
TESTING = True
SESSION_COOKIE_NAME = 'gilmazin_cookie'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'h34v3n'
SECURITY_PASSWORD_SALT = '000'

HOST = "hctf.io"

TEMPLATES_AUTO_RELOAD = True
