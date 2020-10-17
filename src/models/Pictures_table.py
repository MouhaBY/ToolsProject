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


def delete(item):
    dbs.delete_query("Pictures", "id", item)


def get(item):
    sql = "SELECT id, filename, binary, filepath FROM Pictures WHERE id == (?)"
    _result = dbs.execute_query(sql, (item,))
    try:
        return _result.fetchone()
    except TypeError:
        return None


# do not use filename not unique or null
# def ckeck(item):
#     sql = "SELECT id FROM Pictures WHERE filename == (?)"
#     _result = dbs.execute_query(sql, (item,))
#     try:
#         return _result.fetchone()[0]
#     except TypeError:
#         return None

# there is no delete in pictures
# def update(data):
#     sql = """ UPDATE Pictures SET filename= (?), binary= (?), filepath= (?) WHERE id == (?) """
#     dbs.execute_query(sql, data)
