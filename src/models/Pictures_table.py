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
    result_query = dbs.select_one("Pictures", "id", item)
    return result_query
