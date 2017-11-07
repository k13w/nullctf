# flask

## Installation

### Linux:

```
1: $ pip install virtualenv - install the virtualenv
2: $ virtualenv env - create a new virtual enviroment
3: $ source env/bin/activate - activate the virtual environment
4: $ ./prepare.sh - to install dependencies using apt.
5: $ ./gunicorn_start.sh - in a terminal to drop into debug mode.
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

### Add challenge:
```
$ INSERT INTO challenges(name, category, content, flag, score) VALUES ("chall_name", "chall_category", "this is my description of challenge", "HCTF{this_is_a_flag}, 300");
```
