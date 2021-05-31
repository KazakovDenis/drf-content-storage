#!/usr/bin/env bash

set -e
set -u

cd /opt/app

python3 manage.py collectstatic --noinput
python3 manage.py compilemessages --locale ru

dockerize --wait tcp://db:5432 --wait tcp://redis:6379
python3 manage.py migrate --noinput
python3 manage.py create_admin
python3 manage.py load_demo
