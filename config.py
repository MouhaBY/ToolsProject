#! /usr/bin/env python3
# coding: utf-8

# Define the database - we are working with
# SQLite for this example

# sqlite://<nohostname>/<path>
# where <path> is relative:
SQLALCHEMY_DATABASE_URI = 'sqlite:///data/foo.db'
DATABASE_CONNECT_OPTIONS = {}
