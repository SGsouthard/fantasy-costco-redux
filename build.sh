#!/usr/bin/env bash
# exit on error
set -o errexit

pip3 install --upgrade pip
pip3 install django dj-database-url psycopg2-binary 'whitenoise[brotli]' gunicorn
pip3 install -r requirements.txt
# pip3 install 

python3 manage.py collectstatic --no-input
python3 manage.py migrate