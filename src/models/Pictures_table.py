#! /usr/bin/env python3
# coding: utf-8


import src.models.databaseScripts as dbs


def create():
    sql = """ 
    CREATE TABLE "Pictures" (
    "id" INTEGER NOT NULL,
    "filename" TEXT,
    "binary" TEXT,
    "filepath"	TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
    );
    """
    dbs.execute_query(sql)


def add(data):
    sql = """ INSERT INTO Pictures (filename, binary, filepath) values(?, ?, ?); """
    dbs.execute_query(sql, data)
    # return id value of inserted row
    sql_2 = """ SELECT MAX(id) FROM Pictures """
    _result = dbs.execute_query(sql_2)
    try:
        return _result.fetchone()[0]
    except TypeError:
        return None


def delete(item):
    dbs.delete_query("Pictures", "id", item)


def read(item):
    result_query = dbs.select_one("Pictures", "id", item)
    return result_query
