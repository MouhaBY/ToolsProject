#! /usr/bin/env python3
# coding: utf-8


import src.models.databaseScripts as dbs


def create():
    sql = """ 
    CREATE TABLE "Users" (
    "id" INTEGER NOT NULL,
    "username" TEXT NOT NULL UNIQUE,
    "password" TEXT NOT NULL,
    "email" TEXT,
    "contact_id" INTEGER,
    "active" BOOLEAN DEFAULT 'True',
    FOREIGN KEY("contact_id") REFERENCES "Contacts"("id"),
    PRIMARY KEY("id" AUTOINCREMENT)
    );
    """
    dbs.execute_query(sql)


def add(data):
    sql = """ INSERT INTO Users (username, password, email, contact_id, active)
                    values(?, ?, ?, ?, ?) """
    dbs.execute_query(sql, data)


def update(data):
    sql = """ UPDATE Users SET 
    username= (?), password= (?), email= (?), contact_id= (?), active= (?)
    WHERE id == (?) """
    dbs.execute_query(sql, data)


def delete(item):
    dbs.delete_query("Users", "id", item)


def get_id(item):
    result_query = dbs.select_parameter("id", "Users", "username", item)
    return result_query


def get_one(item):
    result_query = dbs.select_one("Users", "id", item)
    return result_query


def get_all():
    result_query = dbs.select_all("Users")
    return result_query


def activate(item, value):
    dbs.activate_query("Users", item, value)
