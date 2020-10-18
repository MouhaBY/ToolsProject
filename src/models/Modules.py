#! /usr/bin/env python3
# coding: utf-8


import src.models.databasescripts as dbs
import src.mvc_exceptions as mvc_exc


class Module:
    def __init__(self, id, name, description, active):
        self.id = id
        self.name = name
        self.description = description
        self.active = active

    def add(self):
        if get_id(self.name) is None:
            insert((self.name, self.description, self.active))
            self.id = get_id(self.name)
            if self.id is not None:
                return 1
            else:
                raise mvc_exc.InsertionError
        else:
            raise mvc_exc.ItemAlreadyExist

    def edit(self):
        if self.id is not None:
            if get_one(self.id) is not None:
                update((self.name, self.description, self.active))
                return 1
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    def remove(self):
        if get_one(self.id) is not None:
            delete(self.id)
            if get_one(self.id) is None:
                return 1
            else:
                raise mvc_exc.DeletionError
        else:
            raise mvc_exc.ItemNotExist

    def activate(self, state):
        if get_one(self.id) is not None:
            if state is bool:
                self.active = state
                activate_sql(("active", self.id, state))
                return 1
            else:
                raise mvc_exc.ParameterUnfilled
        else:
            raise mvc_exc.ItemNotExist

    @staticmethod
    def get_module(item, name=None):
        if item is not None:
            if name is not None:
                item = get_id(item)
            data = get_one(item)
            if data is not None:
                obj_module = Module(data[0], data[1], data[2], data[3])
                return obj_module
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    @staticmethod
    def get_modules():
        modules_list = get_all()
        if modules_list is not None:
            return modules_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def init(data):
        obj_module = Module(data[0], data[1], data[2], data[3])
        return obj_module


""" Database Scripts """


def create():
    sql = """ 
    CREATE TABLE "Modules" (
    "id" INTEGER NOT NULL,
    "name" TEXT NOT NULL UNIQUE,
    "description" TEXT,
    "active" BOOLEAN DEFAULT 'True',
    PRIMARY KEY("id"));
    """
    dbs.execute_query(sql)


def insert(data):
    sql = """ INSERT INTO Modules (name, description, active) values(?, ?, ?); """
    dbs.execute_query(sql, data)


def update(data):
    sql = """ UPDATE Modules SET 
    name= (?), description= (?), active= (?)
    WHERE id == (?) """
    dbs.execute_query(sql, data)


def delete(item):
    dbs.delete_query("Modules", "id", item)


def get_id(item):
    result_query = dbs.select_parameter("id", "Modules", "name", item)
    return result_query


def get_all():
    result_query = dbs.select_all("Modules")
    return result_query


def get_one(item):
    result_query = dbs.select_one("Modules", "id", item)
    return result_query


def activate_sql(data):
    dbs.activate_query("Modules", data[0], data[1])
