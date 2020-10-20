#! /usr/bin/env python3
# coding: utf-8

from src.models import Pictures_model
import src.mvc_exceptions as mvc_exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
import config


Session = sessionmaker(bind=config.engine)
session = Session()


def create(data):
    obj_picture = Pictures_model.Picture(data[0], data[1], data[2])
    session.add(obj_picture)
    session.commit()
    return obj_picture


def read(id):
    obj_picture = session.query(Pictures_model.Picture).get(id)
    if obj_picture is not None:
        return obj_picture
    else:
        raise mvc_exc.ItemNotExist


def delete(object_to_delete):
    session.delete(object_to_delete)
    session.commit()
    check_record_obj = session.query(Pictures_model.Picture).get(object_to_delete.id)
    if check_record_obj is None:
        return 1
    else:
        raise mvc_exc.DeletionError
