#! /usr/bin/env python3
# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
engine.connect()

Session = sessionmaker(bind=engine)
session = Session()
