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
        Pictures.Base.metadata.create_all(engine)

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

    @staticmethod
    def create(image_filepath):
        # Read Image
        with open(image_filepath, "rb") as image:
            f = image.read()
            binary = bytearray(f)
            filename = ''
            filepath = '{}'
            session = session_factory()
            current_obj = Picture(filename, binary, filepath)
            try:
                session.add(current_obj)
                session.commit()
            except:
                session.rollback()
                raise mvc_exc.InsertionError
            finally:
                session.close()
            return current_obj
