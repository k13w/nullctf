from app import app
from os import path, environ

basedir = path.abspath(path.dirname(__file__))

ctf_name = "HCTF"
DEBUG = True
TESTING = True
SESSION_COOKIE_NAME = 'gilmazin_cookie'
environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir,
'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'h34v3n'
SECURITY_PASSWORD_SALT = '000'

HOST = "hctf.io"

TEMPLATES_AUTO_RELOAD = True
