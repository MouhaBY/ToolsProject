#! /usr/bin/env python3
# coding: utf-8

from src.models import Companies
from src.models.Companies import Company
from src.common.db import session_factory, engine
import src.common.mvc_exceptions as mvc_exc


class CompaniesServices(object):
    """Class for managing items in the database"""
    def __init__(self):
        """
        Initializes session and creating tables.
        """
        # engine = create ..??
        # self.session = session_factory(bind=engine)
        Companies.Base.metadata.create_all(engine)
        # self.Session = session_factory()

    @staticmethod
    def create(data):
        session = session_factory()
        current_obj = Company(data[0],data[1], data[2], data[3], data[4],
                              data[5], data[6], data[7], data[8], data[9])
        try:
            # __query_result = session.query(Company).filter(Company.name == current_obj.name).one()
            # if __query_result is None:
            session.add(current_obj)
            session.commit()
            session.close()
            # else:
            #    raise mvc_exc.ItemAlreadyExist
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return current_obj

    @staticmethod
    def read(id_item):
        session = session_factory()
        try:
            current_obj = session.query(Company).get(id_item)
            if current_obj is None:
                raise mvc_exc.ItemNotExist
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return current_obj

    @staticmethod
    def update(current_obj):
        session = session_factory()
        try:
            __query_result = session.query(Company).filter(Company.name == current_obj.name)
            session.commit()
            if __query_result is None:
                raise mvc_exc.ItemAlreadyExist
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return current_obj

    @staticmethod
    def delete(current_obj):
        session = session_factory()
        try:
            session.delete(current_obj)
            session.commit()
            __check_record_obj = session.query(Company).get(current_obj.id)
            if __check_record_obj is not None:
                raise mvc_exc.DeletionError
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return current_obj

    @staticmethod
    def activate(current_obj, state):
        session = session_factory()
        try:
            current_obj.active = state
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return current_obj

    @staticmethod
    def get_companies():
        session = session_factory()
        try:
            companies_list_query = session.query(Company)
            if companies_list_query is None:
                raise mvc_exc.EmptyList
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return companies_list_query.all()
