#! /usr/bin/env python3
# coding: utf-8


import src.models.databasescripts as dbs
import src.mvc_exceptions as mvc_exc


class ActivityLog:
    def __init__(self, users_id, users_username, actions_id, date):
        self.users_id = users_id
        self.users_username = users_username
        self.actions_id = actions_id
        self.date = date

    def add(self):
        insert((self.users_id, self.users_username, self.actions_id, self.date))

    @staticmethod
    def get_activities_list(item):
        if item is not None:
            data = get_list(item)
            if data is not None:
                return data
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    @staticmethod
    def get_activities():
        activities_list = get_all()
        if activities_list is not None:
            return activities_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def init(data):
        obj_activity = ActivityLog(data[0], data[1], data[2], data[3])
        return obj_activity


""" Database Scripts """


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


def insert(data):
    sql = """ INSERT INTO ActivityLog (users_id, users_username, actions_id, descriptions, date) 
    values(?, ?, ?, ?, ?); """
    dbs.execute_query(sql, data)


def get_all():
    result_query = dbs.select_all("ActivityLog")
    return result_query


def get_list(item):
    result_query = dbs.select_list("ActivityLog", "users_id", item)
    return result_query
