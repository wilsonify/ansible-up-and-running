#!/usr/bin/env bash
python3 -m venv venv
# shellcheck disable=SC1091
source venv/bin/activate
pip3 install mezzanine
mezzanine-project myproject
cd myproject || exit
sed -i.bak 's/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = ["127.0.0.1"]/' myproject/settings.py
python3 manage.py createdb
python3 manage.py runserver
