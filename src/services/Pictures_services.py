#! /usr/bin/env python3
# coding: utf-8

import src.common.mvc_exceptions as mvc_exc
from src.common.db import session_factory, engine
from src.models.Pictures import Picture

# to create database tables
from src.models import Pictures


class PicturesServices(object):
    """Class for managing items in the database"""
    def __init__(self):
        """
        Initializes session and creating tables.
        """
        Pictures.Base.metadata.create_all(engine)
        self.current_picture = Picture(None,None,None)

    def read(self, item_id):
        session = session_factory()
        try:
            self.current_picture = session.query(Picture).get(item_id)
        except:
            session.rollback()
            raise
        finally:
            session.close()
        if self.current_picture is not None:
            return self.current_picture
        else:
            raise mvc_exc.ItemNotExist

    def create(self, image_filepath):
        # Read Image
        with open(image_filepath, "rb") as image:
            f = image.read()
            binary = bytearray(f)
            filename = ''
            session = session_factory()
            self.current_picture = Picture(filename, binary, image_filepath)
            try:
                session.add(self.current_picture)
                session.commit()
            except:
                session.rollback()
                raise mvc_exc.InsertionError
            finally:
                session.close()
            return self.current_picture
