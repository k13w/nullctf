# flask

## Usage

### Linux:

```
$ git clone https://github.com/HeavenH/flask.git
$ cd flask
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python manage.py runserver
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

### Add challenge:
```
$ INSERT INTO challenges(name, category, content, flag, score) VALUES ("chall_name", "chall_category", "this is my description of challenge", "HCTF{this_is_a_flag}, 300");
```
