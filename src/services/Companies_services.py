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
        Companies.Base.metadata.create_all(engine)
        self.current_company = Company(None, None, None, None, None, None, None, None, None, None)

    def create(self):
        session = session_factory()
        try:
            __query_result = session.query(Company).filter(Company.name == self.current_company.name).first()
            if __query_result is None:
                session.add(self.current_company)
                session.commit()
            else:
                raise mvc_exc.ItemAlreadyExist
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return self.current_company

    def get(self, id_item):
        session = session_factory()
        try:
            self.current_company = session.query(Company).get(id_item)
            if self.current_company is None:
                raise mvc_exc.ItemNotExist
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return self.current_company

    def update(self):
        session = session_factory()
        try:
            __query_result = session.query(Company).filter(Company.name == self.current_company.name).first()
            if __query_result is None:
                session.close()
                session = session_factory()
                try:
                    __check_record_obj = session.query(Company).get(self.current_company.id)
                    __check_record_obj.name = self.current_company.name
                    __check_record_obj.code = self.current_company.code
                    __check_record_obj.address = self.current_company.address
                    __check_record_obj.registration = self.current_company.registration
                    __check_record_obj.phone = self.current_company.phone
                    __check_record_obj.mobile = self.current_company.mobile
                    __check_record_obj.website = self.current_company.website
                    __check_record_obj.mail = self.current_company.mail
                    # __check_record_obj.picture = self.current_company.picture
                    __check_record_obj.active = self.current_company.active
                    session.commit()
                    self.current_company = __check_record_obj
                except:
                    session.rollback()
                    raise
            else:
                raise mvc_exc.ItemAlreadyExist
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return self.current_company

    def delete(self):
        session = session_factory()
        try:
            session.delete(self.current_company)
            session.commit()
            __check_record_obj = session.query(Company).get(self.current_company.id)
            if __check_record_obj is not None:
                raise mvc_exc.DeletionError
            self.current_company = __check_record_obj
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return self.current_company

    def activate(self, state):
        session = session_factory()
        try:
            __check_record_obj = session.query(Company).get(self.current_company.id)
            __check_record_obj.active = state
            session.commit()
            self.current_company = __check_record_obj
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return self.current_company

    @staticmethod
    def get_companies():
        session = session_factory()
        try:
            __companies_list_query = session.query(Company)
            companies_list = __companies_list_query.all()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return companies_list
