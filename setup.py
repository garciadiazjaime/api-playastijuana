#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='playastijuana',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='API with business located at Playas de Tijuana',
    # GETTING-STARTED: set author name (your name):
    author='Jaime Garcia Diaz',
    # GETTING-STARTED: set author email (your email):
    author_email='garciadiazjaime@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.challenge202.com/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.8.4'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
