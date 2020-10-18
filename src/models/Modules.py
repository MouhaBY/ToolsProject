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
        if Module.__get_id_by_name(self.name) is None:
            Module.__insert((self.name, self.description, self.active))
            self.id = Module.__get_id_by_name(self.name)
            if self.id is not None:
                return 1
            else:
                raise mvc_exc.InsertionError
        else:
            raise mvc_exc.ItemAlreadyExist

    def edit(self):
        if self.id is not None:
            if Module.__get_one(self.id) is not None:
                Module.__update((self.name, self.description, self.active))
                return 1
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    def remove(self):
        if Module.__get_one(self.id) is not None:
            dbs.delete_query("Profiles_Modules", "modules_id", self.id)
            dbs.delete_query("Modules", "id", self.id)
            if Module.__get_one(self.id) is None:
                return 1
            else:
                raise mvc_exc.DeletionError
        else:
            raise mvc_exc.ItemNotExist

    def activate(self, state):
        if Module.__get_one(self.id) is not None:
            if state is bool:
                self.active = state
                dbs.activate_query("Modules", state, self.id)
                return 1
            else:
                raise mvc_exc.ParameterUnfilled
        else:
            raise mvc_exc.ItemNotExist

    @staticmethod
    def get_module(item, name=None):
        if item is not None:
            if name is not None:
                item = Module.__get_id_by_name(item)
            data = Module.__get_one(item)
            if data is not None:
                obj_module = Module(data[0], data[1], data[2], data[3])
                return obj_module
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    @staticmethod
    def get_modules():
        modules_list = dbs.select_all("Modules")
        if modules_list is not None:
            return modules_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def init(data):
        obj_module = Module(data[0], data[1], data[2], data[3])
        return obj_module

    # """ Database Scripts """
    @staticmethod
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

    @staticmethod
    def __insert(data):
        sql = """ INSERT INTO Modules (name, description, active) values(?, ?, ?); """
        dbs.execute_query(sql, data)

    @staticmethod
    def __update(data):
        sql = """ UPDATE Modules SET 
        name= (?), description= (?), active= (?)
        WHERE id == (?) """
        dbs.execute_query(sql, data)

    @staticmethod
    def __get_id_by_name(item):
        result_query = dbs.select_parameter("id", "Modules", "name", item)
        return result_query

    @staticmethod
    def __get_one(item):
        result_query = dbs.select_one("Modules", "id", item)
        return result_query
