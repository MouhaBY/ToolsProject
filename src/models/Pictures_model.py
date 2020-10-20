#! /usr/bin/env python3
# coding: utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, BLOB, table


Base = declarative_base()


class Picture(Base):
    __tablename__ = 'Pictures'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    binary = Column(BLOB)
    filepath = Column(String)

    def __init__(self, filename, binary, filepath):
        self.id = None
        self.filename = filename
        self.binary = binary
        self.filepath = filepath
