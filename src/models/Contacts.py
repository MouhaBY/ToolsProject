#! /usr/bin/env python3
# coding: utf-8


import src.scripts.databasescripts as dbs
import src.common.mvc_exceptions as mvc_exc


class Contact:
    def __init__(self, id, name, subname, address, registration,
                 phone, mobile, function, companies_id, pictures_id, active):
        self.id = id
        self.name = name
        self.subname = subname
        self.address = address
        self.registration = registration
        self.phone = phone
        self.mobile = mobile
        self.function = function
        self.companies_id = companies_id
        self.pictures_id = pictures_id
        self.active = active

    def add(self):
        self.id = Contact.__insert((self.name, self.subname, self.address, self.registration, self.phone,
                                    self.mobile, self.function, self.companies_id, self.pictures_id, self.active))
        if self.id is not None:
            return 1
        else:
            raise mvc_exc.InsertionError

    def edit(self):
        if self.id is not None:
            if Contact.__get_one(self.id) is not None:
                Contact.__update((self.name, self.subname, self.address, self.registration, self.phone,
                                  self.mobile, self.function, self.companies_id, self.pictures_id, self.active,
                                  self.id))
                return 1
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    def remove(self):
        if self.id is not None:
            if Contact.__get_one(self.id) is not None:
                dbs.delete_query("Contacts", "id", self.id)
                if Contact.__get_one(self.id) is None:
                    return 1
                else:
                    raise mvc_exc.DeletionError
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    def activate(self, state):
        if Contact.__get_one(self.id) is not None:
            if state is bool:
                self.active = state
                dbs.activate_query("Contacts", state, self.id)
                return 1
            else:
                raise mvc_exc.ParameterUnfilled
        else:
            raise mvc_exc.ItemNotExist

    """ static method"""

    @staticmethod
    def get_contact(item):
        if item is not None:
            data = Contact.__get_one(item)
            if data is not None:
                obj_contact = Contact(data[0], data[1], data[2], data[3], data[4],
                                      data[5], data[6], data[7], data[8], data[9], data[10])
                return obj_contact
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    @staticmethod
    def get_contacts():
        contacts_list = dbs.select_all("Contacts")
        if contacts_list is not None:
            return contacts_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def init(data):
        obj_contact = Contact(data[0], data[1], data[2], data[3], data[4],
                              data[5], data[6], data[7], data[8], data[9], data[10])
        return obj_contact

# """ Database scripts """
    @staticmethod
    def create():
        sql = """ 
        CREATE TABLE "Contacts" (
         "id" INTEGER NOT NULL,
         "name" TEXT NOT NULL,
         "subname" TEXT,
         "address" TEXT,
         "registration"	TEXT,
         "phone" TEXT,
         "mobile" TEXT,
         "function"	TEXT,
         "companies_id"	INTEGER,
         "pictures_id" INTEGER,
         "active" BOOLEAN DEFAULT 'True',
         FOREIGN KEY("companies_id") REFERENCES "Companies"("id"),
         FOREIGN KEY("pictures_id") REFERENCES "Pictures"("id"),
         PRIMARY KEY("id" AUTOINCREMENT)
        ); """
        dbs.execute_query(sql)

    @staticmethod
    def __insert(data):
        sql = """ INSERT INTO Contacts 
            (name, subname, address, registration, phone, 
            mobile, function, companies_id, pictures_id, active)
                        values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
        dbs.execute_query(sql, data)
        # return id value of inserted row
        sql_2 = """ SELECT MAX(id) FROM Contacts """
        _result = dbs.execute_query(sql_2)
        try:
            return _result.fetchone()[0]
        except TypeError:
            return None

    @staticmethod
    def __get_one(item):
        result_query = dbs.select_one("Contacts", "id", item)
        return result_query

    @staticmethod
    def __update(data):
        sql = """ UPDATE Contacts SET 
        name= (?), subname= (?), address= (?), registration= (?), phone= (?), 
        mobile= (?), function= (?), companies_id= (?), pictures_id= (?), active= (?)
        WHERE id == (?) """
        dbs.execute_query(sql, data)
