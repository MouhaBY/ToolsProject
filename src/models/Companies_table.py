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
    "active" BOOLEAN NOT NULL DEFAULT 'True',
    PRIMARY KEY("id" AUTOINCREMENT)
    );
    """
    dbs.execute_query(sql)


def add(data):
    sql = """ INSERT INTO Companies (name, code, address, registration, phone, mobile, website, mail, active)
                values(?, ?, ?, ?, ?, ?, ?, ?, ?) """
    dbs.execute_query(sql, data)
