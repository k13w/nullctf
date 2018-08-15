# Null CTF
[![Python-Versions](https://img.shields.io/badge/python-2.7%2C%203.3%2C%203.4%2C%203.5-blue.svg)](https://www.python.org/)
[![Version-Program](https://img.shields.io/badge/version-1.1-orange.svg)](https://github.com/HeavenH/flask/releases)
[![build](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/HeavenH/flask)

## Features:
```
18-04-2018 -> add OAuth with providers
```

## Installation

```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install --upgrade -r requirements.txt
$ chmod +x db.sh gunicorn_start.sh
$ ./db.sh
$ ./start.sh
```

### OAuth Config:

```
Change api.ini with your client_id and client_secret
```

Usage:

### Setup API key
```
$ export RECAPTCHA_PRIVATE_KEY='<your recaptcha private key>'
$ export RECAPTCHA_PUBLIC_KEY='< your recaptcha public key>'
```
