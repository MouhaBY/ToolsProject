#! /usr/bin/env python3
# coding: utf-8

from sqlalchemy import Column, Integer, String, BLOB

from src.common.db import Base


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

    def __repr__(self):
        return '<Picture {}>'.format(self.filepath)
