# flask
[![Python-Versions](https://img.shields.io/badge/python-2.7%2C%203.3%2C%203.4%2C%203.5-blue.svg)](https://www.python.org/)
[![Version-Program](https://img.shields.io/badge/version-1.1-orange.svg)](https://github.com/HeavenH/flask/releases)
[![Build](https://img.shields.io/badge/build-passing-33ccff.svg)
![PyPI](https://img.shields.io/pypi/v/nine.svg)
## What is HCTF?

HCTF is a Capture The Flag jeopardy style CTF. Developed in flask, so simple to install and play, enjoy :p

## Features:
```
18-04-2018 -> add OAuth with providers
```

## Installation

### Linux:

```
$ pip install virtualenv
$ virtualenv venv
$ source env/bin/activate
$ pip install --upgrade -r requirements.txt
$ ./prepare.sh
$ ./gunicorn_start.sh
```
### Windows:
```
$ pip install virtualenv
$ virtualenv venv
$ cd env/scripts
$ activate
$ pip install --upgrade -r requirements.txt
$ manage.py db init
$ manage.py db migrate
$ manage.py db upgrade
$ manage.py runserver
```

Usage:

### Setup API key
```
$ export RECAPTCHA_PRIVATE_KEY='<your recaptcha private key>'
$ export RECAPTCHA_PUBLIC_KEY='< your recaptcha public key>'
```
