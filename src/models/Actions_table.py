#! /usr/bin/env python3
# coding: utf-8


import src.models.databaseScripts as dbs


def create():
    sql = """ 
    CREATE TABLE "Actions" (
    "id" INTEGER NOT NULL,
    "name" TEXT NOT NULL UNIQUE,
    "description" TEXT,
    "active" BOOLEAN DEFAULT 'True',
    PRIMARY KEY("id")
    );
    """
    dbs.execute_query(sql)


def add(data):
    sql = """ INSERT INTO Actions (name, description, active) values(?, ?, ?); """
    dbs.execute_query(sql, data)


def update(data):
    sql = """ UPDATE Actions SET 
    name= (?), description= (?), active= (?)
    WHERE id == (?) """
    dbs.execute_query(sql, data)


def delete(item):
    dbs.delete_query("Actions", "id", item)


def get_id(item):
    result_query = dbs.select_parameter("id", "Actions", "name", item)
    return result_query


def get_all():
    result_query = dbs.select_all("Actions")
    return result_query


def get(item):
    result_query = dbs.select_one("Actions", "id", item)
    return result_query


def activate(item, value):
    dbs.activate_query("Actions", item, value)