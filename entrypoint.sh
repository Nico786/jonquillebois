#!/bin/sh

python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input

gunicorn project.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 90 --log-file gunicorn.log --log-level debug