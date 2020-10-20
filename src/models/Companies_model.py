#! /usr/bin/env python3
# coding: utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN


Base = declarative_base()


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
    pictures_id = Column(Integer)
    #pictures_id = Column(Integer, ForeignKey('Pictures.id'))
    # Picture = relationship("Picture")
    active = Column(BOOLEAN, default=1)

    def __init__(self, name, code, address, registration, phone, mobile, website, mail, pictures_id, active):
        self.id = None
        self.name = name
        self.code = code
        self.address = address
        self.registration = registration
        self.phone = phone
        self.mobile = mobile
        self.website = website
        self.mail = mail
        self.pictures_id = pictures_id
        self.active = active
