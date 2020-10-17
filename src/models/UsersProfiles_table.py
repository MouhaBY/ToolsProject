#! /usr/bin/env python3
# coding: utf-8


import src.models.databaseScripts as dbs


def create():
    sql = """
    CREATE TABLE "Users_Profiles" (
    "users_id" INTEGER NOT NULL,
    "profiles_id" INTEGER NOT NULL,
    PRIMARY KEY("users_id","profiles_id"),
    FOREIGN KEY("users_id") REFERENCES "Users"("id"),
    FOREIGN KEY("profiles_id") REFERENCES "Profiles"("id")
    );
    """
    dbs.execute_query(sql)


def affect(data):
    sql = """ INSERT INTO Users_Profiles (users_id, profiles_id) values(?, ?); """
    dbs.execute_query(sql, data)


def disaffect(item):
    dbs.delete_query("Users_Profiles", "profiles_id", item)


def get_all():
    result_query = dbs.select_all("Users_Profiles")
    return result_query


def get_list(item):
    result_query = dbs.select_list("Users_Profiles", "users_id", item)
    return result_query
