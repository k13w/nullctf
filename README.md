# flask
[![Python-Versions](https://img.shields.io/badge/python-2.7%2C%203.3%2C%203.4%2C%203.5-blue.svg)](https://www.python.org/)
[![Version-Program](https://img.shields.io/badge/version-1.0-orange.svg)](https://github.com/HeavenH/flask/releases)
[![Build](https://img.shields.io/badge/build-passing-33ccff.svg)
## What is HCTF?

HCTF is a Capture The Flag jeopardy style CTF. Developed in flask, so simple to install and play, enjoy :p
## Installation

### Linux:

```
$ pip install virtualenv
$ virtualenv env
$ source env/bin/activate
$ ./prepare.sh
$ ./gunicorn_start.sh
```
### Windows:
```
$ pip install virtualenv
$ virtualenv env
$ cd env/scripts
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
