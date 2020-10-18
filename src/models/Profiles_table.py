#! /usr/bin/env python3
# coding: utf-8


import src.models.databasescripts as dbs


def create():
    sql = """ 
    CREATE TABLE "Profiles" (
    "id" INTEGER NOT NULL,
    "name" TEXT NOT NULL UNIQUE,
    "description" TEXT,
    "active" BOOLEAN DEFAULT 'True',
    PRIMARY KEY("id" AUTOINCREMENT));
    """
    dbs.execute_query(sql)


def add(data):
    sql = """ INSERT INTO Profiles (name, description, active) values(?, ?, ?); """
    dbs.execute_query(sql, data)


def update(data):
    sql = """ UPDATE Profiles SET 
    name= (?), description= (?), active= (?)
    WHERE id == (?) """
    dbs.execute_query(sql, data)


def delete(item):
    dbs.delete_query("Profiles", "id", item)


def get_id(item):
    result_query = dbs.select_parameter("id", "Profiles", "name", item)
    return result_query


def get_all():
    result_query = dbs.select_all("Profiles")
    return result_query


def get(item):
    result_query = dbs.select_one("Profiles", "id", item)
    return result_query


def activate(data):
    dbs.activate_query("Profiles", data[0], data[1])
