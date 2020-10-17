#! /usr/bin/env python3
# coding: utf-8


import src.models.databaseScripts as dbs


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


def add(data):
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


def activate(data):
    dbs.activate_query("Companies", data[0], data[1])
