#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pippip install --force-reinstall -U setuptools

python3 manage.py collectstatic --no-input
python3 manage.py migrate