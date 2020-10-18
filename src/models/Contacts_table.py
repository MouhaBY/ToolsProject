#! /usr/bin/env python3
# coding: utf-8


import src.models.databasescripts as dbs


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


def add(data):
    sql = """ INSERT INTO Contacts 
        (name, subname, address, registration, phone, 
        mobile, function, companies_id, pictures_id, active)
                    values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
    dbs.execute_query(sql, data)


def delete(item):
    dbs.delete_query("Contacts", "id", item)


def get_one(item):
    result_query = dbs.select_one("Contacts", "id", item)
    return result_query


def update(data):
    sql = """ UPDATE Contacts SET 
    name= (?), subname= (?), address= (?), registration= (?), phone= (?), 
    mobile= (?), function= (?), companies_id= (?), pictures_id= (?), active= (?)
    WHERE id == (?) """
    dbs.execute_query(sql, data)


# Do not know on which parmater to search
# def get_id(item):
#     result_query = dbs.select_parameter("id", "Contacts", "name", item)
#     return result_query


def get_all():
    result_query = dbs.select_all("Contacts")
    return result_query


def activate(data):
    dbs.activate_query("Contacts", data[0], data[1])
