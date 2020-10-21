#! /usr/bin/env python3
# coding: utf-8

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN

from src.common.db import Base
from src.models.Pictures import Picture


class Company(Base):
    __tablename__ = "Companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    code = Column(String)
    address = Column(String)
    registration = Column(String)
    phone = Column(String)
    mobile = Column(String)
    website = Column(String)
    mail = Column(String)
    # pictures_id = Column(Integer)
    pictures_id = Column(Integer, ForeignKey('Pictures.id'))
    picture = relationship("Picture", primaryjoin=pictures_id == Picture.id)
    active = Column(BOOLEAN, default=1)

    def __init__(self, name, code, address, registration, phone, mobile, website, mail, picture, active):
        self.id = None
        self.name = name
        self.code = code
        self.address = address
        self.registration = registration
        self.phone = phone
        self.mobile = mobile
        self.website = website
        self.mail = mail
        self.picture = picture
        self.active = active

    def __repr__(self):
        return '<Company - name : {}>'.format(self.name)
