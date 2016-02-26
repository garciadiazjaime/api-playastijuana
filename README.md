Playas de Tijuana API
====

[![Build Status](https://travis-ci.org/garciadiazjaime/api-playastijuana.svg)](https://travis-ci.org/garciadiazjaime/api-playastijuana)

API with business located at Playas de Tijuana

Technologies:
django + djangorest


Package Installation
`pip install -r requirements.txt`

Run Server
`cd project`
`python manage.py runserver`

GUI - Admin
http://127.0.0.1:8000/admin

DB Setup
`psql -c create database `
`python manage.py migrate`
`python manage.py createsuperuser` (this is the user for access the admin, feel free to type anything)
`python manage.py loaddata fixtures.json` (warnings are OK)
