#! /usr/bin/env python3
# coding: utf-8

from src.models import Pictures
from src.models.Pictures import Picture
import src.common.mvc_exceptions as mvc_exc
from src.common.db import session_factory, engine


class PicturesServices(object):
    """Class for managing items in the database"""
    def __init__(self):
        """
        Initializes session and creating tables.
        """
        # engine = create ..??
        # self.session = session_factory(bind=engine)
        Pictures.Base.metadata.create_all(engine)
        # session = session_factory(engine)

    @staticmethod
    def create(data):
        session = session_factory()
        current_obj = Picture(data[0], data[1], data[2])
        try:
            session.add(current_obj)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return current_obj

    @staticmethod
    def read(item_id):
        session = session_factory()
        try:
            current_obj = session.query(Picture).get(item_id)
        except:
            session.rollback()
            raise
        finally:
            session.close()
        if current_obj is not None:
            return current_obj
        else:
            raise mvc_exc.ItemNotExist
