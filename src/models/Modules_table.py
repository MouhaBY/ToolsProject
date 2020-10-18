#! /usr/bin/env python3
# coding: utf-8


import src.models.databasescripts as dbs


def create():
    sql = """ 
    CREATE TABLE "Modules" (
    "id" INTEGER NOT NULL,
    "name" TEXT NOT NULL UNIQUE,
    "description" TEXT,
    "active" BOOLEAN DEFAULT 'True',
    PRIMARY KEY("id"));
    """
    dbs.execute_query(sql)


def add(data):
    sql = """ INSERT INTO Modules (name, description, active) values(?, ?, ?); """
    dbs.execute_query(sql, data)


def update(data):
    sql = """ UPDATE Modules SET 
    name= (?), description= (?), active= (?)
    WHERE id == (?) """
    dbs.execute_query(sql, data)


def delete(item):
    dbs.delete_query("Modules", "id", item)


def get_id(item):
    result_query = dbs.select_parameter("id", "Modules", "name", item)
    return result_query


def get_all():
    result_query = dbs.select_all("Modules")
    return result_query


def get(item):
    result_query = dbs.select_one("Modules", "id", item)
    return result_query


def activate(data):
    dbs.activate_query("Modules", data[0], data[1])
