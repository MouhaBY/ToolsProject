#! /usr/bin/env python3
# coding: utf-8


import src.models.databaseScripts as dbs


def create():
    sql = """
    CREATE TABLE "Profiles_Modules" (
    "profiles_id" INTEGER NOT NULL,
    "modules_id" INTEGER NOT NULL,
    FOREIGN KEY("modules_id") REFERENCES "Modules"("id"),
    PRIMARY KEY("profiles_id","modules_id"),
    FOREIGN KEY("profiles_id") REFERENCES "Profiles"("id")
    );
    """
    dbs.execute_query(sql)


def affect(data):
    sql = """ INSERT INTO Profiles_Modules (profiles_id, modules_id) values(?, ?); """
    dbs.execute_query(sql, data)


def disaffect(item):
    dbs.delete_query("Profiles_Modules", "modules_id", item)


def get_all():
    result_query = dbs.select_all("Profiles_Modules")
    return result_query


def get_list(item):
    result_query = dbs.select_list("Profiles_Modules", "profiles_id", item)
    return result_query
