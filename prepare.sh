#!/bin/sh
sudo apt-get update
virtualenv env
source env/bin/activate
pip install -r requirements.txt