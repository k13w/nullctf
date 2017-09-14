from app import app
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'H34V3N-F14SK-S3CR3T'
SECURITY_PASSWORD_SALT = 'my_s3cUr3_s4lt'
