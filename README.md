# flask

## What is HCTF?

HCTF is a Capture The Flag jeopardy style CTF. Developed in flask, so simple to install and play, enjoy :p
## Installation

### Linux:

```
$ pip install virtualenv - install the virtualenv
$ virtualenv env - create a new virtual enviroment
$ source env/bin/activate - activate the virtual environment
$ ./prepare.sh - to install dependencies using apt.
$ ./gunicorn_start.sh - run app in a terminal to drop into debug mode.
```
### Windows:
```
$ git clone https://github.com/HeavenH/flask.git
$ cd flask
$ pip install virtualenv
$ virtualenv venv
$ cd venv/scripts
$ activate
$ pip install -r requirements.txt
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python manage.py runserver
```

Usage:

### Setup API key
```
$ export RECAPTCHA_PRIVATE_KEY='<your recaptcha private key>'
$ export RECAPTCHA_PUBLIC_KEY='< your recaptcha public key>'
```
