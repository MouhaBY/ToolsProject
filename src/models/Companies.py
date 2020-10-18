#! /usr/bin/env python3
# coding: utf-8


import src.models.databasescripts as dbs
import src.mvc_exceptions as mvc_exc


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
        # if self.pictures_id is not None:
        #      self.picture = get(self.pictures_id)

    def add(self):
        if get_id(self.name) is None:
            insert((self.name, self.code, self.address, self.registration, self.phone,
                    self.mobile, self.website, self.mail, self.pictures_id, self.active))
            self.id = get_id(self.name)
            if self.id is not None:
                return 1
            else:
                raise mvc_exc.InsertionError
        else:
            raise mvc_exc.ItemAlreadyExist

    def edit(self):
        if self.id is not None:
            if get_one(self.id) is not None:
                update((self.name, self.code, self.address, self.registration, self.phone,
                        self.mobile, self.website, self.mail, self.pictures_id, self.active, self.id))
                return 1
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    def remove(self):
        if get_one(self.id) is not None:
            delete(self.id)
            if get_id(self.id) is None:
                return 1
            else:
                raise mvc_exc.DeletionError
        else:
            raise mvc_exc.ItemNotExist

    def activate(self, state):
        if get_one(self.id) is not None:
            if state is bool:
                self.active = state
                activate_sql(("active", self.id, state))
                return 1
            else:
                raise mvc_exc.ParameterUnfilled
        else:
            raise mvc_exc.ItemNotExist

    @staticmethod
    def get_company(item, name=None):
        if item is not None:
            if name is not None:
                item = get_id(item)
            data = get_one(item)
            if data is not None:
                obj_company = Company(data[0], data[1], data[2], data[3], data[4],
                                      data[5], data[6], data[7], data[8], data[9], data[10])
                return obj_company
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    @staticmethod
    def get_companies():
        companies_list = get_all()
        if companies_list is not None:
            return companies_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def init(data):
        obj_company = Company(data[0], data[1], data[2], data[3], data[4],
                              data[5], data[6], data[7], data[8], data[9], data[10])
        return obj_company


""" DATABASE QUERIES TO MANIPULATE DATA """


# Database Scripts
def create():
    sql = """ 
    CREATE TABLE "Companies" (
    "id" INTEGER NOT NULL, 
    "name" TEXT NOT NULL UNIQUE,
    "code" TEXT,
    "address" TEXT, 
    "registration" TEXT,
    "phone" TEXT,
    "mobile" TEXT,
    "website" TEXT,
    "mail" TEXT,
    "pictures_id" INTEGER,
    "active" BOOLEAN DEFAULT 'True',
    FOREIGN KEY("pictures_id") REFERENCES "Pictures"("id"),
    PRIMARY KEY("id" AUTOINCREMENT)
    );
    """
    dbs.execute_query(sql)


def insert(data):
    sql = """ 
    INSERT INTO Companies (name, code, address, registration, phone, mobile, website, mail, pictures_id, active)
                values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
    dbs.execute_query(sql, data)


def delete(item):
    dbs.delete_query("Companies", "id", item)


def get_one(item):
    result_query = dbs.select_one("Companies", "id", item)
    return result_query


def update(data):
    sql = """ UPDATE Companies SET 
    name= (?), code= (?), address= (?), registration= (?), phone= (?), mobile= (?), website= (?), mail= (?), 
    pictures_id= (?), active= (?)
    WHERE id == (?) """
    dbs.execute_query(sql, data)


def get_id(item):
    result_query = dbs.select_parameter("id", "Companies", "name", item)
    return result_query


def get_all():
    result_query = dbs.select_all("Companies")
    return result_query


def activate_sql(data):
    dbs.activate_query("Companies", data[0], data[1])
