#! /usr/bin/env python3
# coding: utf-8


import src.models.databaseScripts as dbs


def create():
    sql = """ 
    CREATE TABLE "Users" (
    "id" INTEGER NOT NULL,
    "username" TEXT NOT NULL UNIQUE,
    "password"	TEXT NOT NULL,
    "email" TEXT,
    "contact_id" INTEGER,
    "active" BOOLEAN NOT NULL DEFAULT 'True',
    PRIMARY KEY("id" AUTOINCREMENT)
    );
     """
    dbs.execute_query(sql)


def add(data):
    sql = """ INSERT INTO Users (username, password, email, contact_id, active)
                    values(?, ?, ?, ?, ?) """
    dbs.execute_query(sql, data)
