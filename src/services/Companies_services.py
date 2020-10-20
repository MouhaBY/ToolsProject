#! /usr/bin/env python3
# coding: utf-8

from src.models import Companies_model
import src.mvc_exceptions as mvc_exc
from sqlalchemy.sql.expression import func
from src import session


def create(data):
    current_obj = Companies_model.Company(data[0], data[1], data[2], data[3], data[4],
                                          data[5], data[6], data[7], data[8], data[9])
    q = session.query(Companies_model.Company).filter(Companies_model.Company.name == current_obj.name).one()
    if q is None:
        session.add(current_obj)
        session.commit()
        return current_obj
    else:
        raise mvc_exc.ItemAlreadyExist


def read(id):
    current_obj = session.query(Companies_model.Company).get(id)
    if current_obj is not None:
        return current_obj
    else:
        raise mvc_exc.ItemNotExist


def update(object_to_update):
    q = session.query(Companies_model.Company).filter(Companies_model.Company.name == object_to_update.name)
    if q is None:
        session.commit()
        return 1
    else:
        raise mvc_exc.ItemAlreadyExist


def delete(object_to_delete):
    session.delete(object_to_delete)
    session.commit()
    check_record_obj = session.query(Companies_model.Company).get(object_to_delete.id)
    if check_record_obj is None:
        return 1
    else:
        raise mvc_exc.DeletionError


def activate(object_to_state, state):
    if state is bool:
        object_to_state.active = state
        session.commit()
        return 1
    else:
        raise mvc_exc.ParameterUnfilled


def get_companies():
    companies_list = session.query(Companies_model.Company).all()
    if companies_list is not None:
        return companies_list
    else:
        raise mvc_exc.EmptyList
