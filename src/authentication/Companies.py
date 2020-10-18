#! /usr/bin/env python3
# coding: utf-8

import src.models.Companies_table as Companies_table
import src.authentication.Pictures as Pictures


class Company:
    def __init__(self, id, name, code, address, registration, phone, mobile, website, mail, pictures_id, active):
        self.id = id
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
        # Determine company image
        if self.pictures_id is not None:
            self.picture = Pictures.get(self.pictures_id)

    def add(self):
        if Companies_table.get_id(self.name) is None:
            Companies_table.add((self.name, self.code, self.address, self.registration, self.phone,
                                 self.mobile,self.website, self.mail, self.pictures_id, self.active))
            self.id = Companies_table.get_id(self.name)
            if self.id is not None:
                return 1

    def delete(self):
        self.id = Companies_table.get_id(self.name)
        if self.id is not None:
            Companies_table.delete(self.id)
            if Companies_table.get_id(self.name) is None:
                return 1

    def update(self):
        self.id = Companies_table.get_id(self.name)
        if self.id is not None:
            Companies_table.update((self.name, self.code, self.address, self.registration, self.phone, self.mobile,
                                    self.website, self.mail, self.pictures_id, self.active, self.id))
            return 1

    def activate(self,state):
        self.id = Companies_table.get_id(self.name)
        if self.id is not None:
            self.active=state
            Companies_table.activate(("active",self.id, state))
            return 1


def get_company(item):
    data = Companies_table.get_one(item)
    if data is not None:
        obj_company = Company(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9],
                              data[10])
        return obj_company


def get_companies():
    data_list = Companies_table.get_all()
    return data_list


def init(data):
    obj_company = Company(None, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])
    return obj_company
