#!/bin/sh
sudo apt-get update
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
