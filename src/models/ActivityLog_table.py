#! /usr/bin/env python3
# coding: utf-8


import src.models.databaseScripts as dbs


def create():
    sql = """ 
    CREATE TABLE "ActivityLog" (
    "users_id"	INTEGER NOT NULL,
    "users_username" TEXT NOT NULL,
    "actions_id" INTEGER NOT NULL,
    "descriptions" TEXT,
    "date" TEXT NOT NULL
    );
    """
    dbs.execute_query(sql)


def add(data):
    sql = """ INSERT INTO ActivityLog (users_id, users_username, actions_id, descriptions, date) 
    values(?, ?, ?, ?, ?); """
    dbs.execute_query(sql, data)


def get_all():
    result_query = dbs.select_all("ActivityLog")
    return result_query


def get_list(item):
    result_query = dbs.select_one("ActivityLog", "users_id", item)
    return result_query
