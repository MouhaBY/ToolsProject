#! /usr/bin/env python3
# coding: utf-8

from src.models import Pictures_model
import src.mvc_exceptions as mvc_exc
from sqlalchemy.orm import sessionmaker
import config


Session = sessionmaker(bind=config.engine)
session = Session()


def create(data):
    current_obj = Pictures_model.Picture(data[0], data[1], data[2])
    session.add(current_obj)
    session.commit()
    return current_obj


def read(id):
    current_obj = session.query(Pictures_model.Picture).get(id)
    if current_obj is not None:
        return current_obj
    else:
        raise mvc_exc.ItemNotExist
