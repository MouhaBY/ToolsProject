#! /usr/bin/env python3
# coding: utf-8


import src.models.databaseScripts as dbs


def create():
    sql = """ 
    CREATE TABLE "Contacts" (
     "id" INTEGER NOT NULL,
     "name" TEXT NOT NULL,
     "subname" TEXT,
     "address" TEXT,
     "registration"	TEXT,
     "phone" TEXT,
     "mobile" TEXT,
     "companies_id"	INTEGER,
     "function"	TEXT,
     "active" BOOLEAN NOT NULL DEFAULT 'True',
     FOREIGN KEY("companies_id") REFERENCES "Companies"("id"),
     PRIMARY KEY("id" AUTOINCREMENT)
    ); """
    dbs.execute_query(sql)


def add(data):
    sql = """ INSERT INTO Contacts (name, subname, address, registration, phone, mobile, companies_id, function, active)
                    values(?, ?, ?, ?, ?, ?, ?, ?, ?) """
    dbs.execute_query(sql, data)
