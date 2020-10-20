#! /usr/bin/env python3
# coding: utf-8

from sqlalchemy import create_engine


# sqlite://<nohostname>/<path>
# where <path> is relative:
SQLALCHEMY_DATABASE_URI = 'sqlite:///data/foo.db'


def sqlalchemy_database():
    __engine = create_engine(SQLALCHEMY_DATABASE_URI)
    __engine.connect()
    return __engine


engine = sqlalchemy_database()
