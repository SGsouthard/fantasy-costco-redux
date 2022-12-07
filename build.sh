#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip

python3 manage.py collectstatic --no-input
python3 manage.py migrate