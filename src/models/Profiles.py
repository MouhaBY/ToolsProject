#! /usr/bin/env python3
# coding: utf-8


import src.scripts.databasescripts as dbs
import src.common.mvc_exceptions as mvc_exc


class Profile:
    def __init__(self, id, name, description, active):
        self.id = id
        self.name = name
        self.description = description
        self.active = active

    def add(self):
        if Profile.__get_id_by_name(self.name) is None:
            Profile.__insert((self.name, self.description, self.active))
            self.id = Profile.__get_id_by_name(self.name)
            if self.id is not None:
                return 1
            else:
                raise mvc_exc.InsertionError
        else:
            raise mvc_exc.ItemAlreadyExist

    def edit(self):
        if self.id is not None:
            if Profile.__select_one(self.id) is not None:
                Profile.__update((self.name, self.description, self.active))
                return 1
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    def remove(self):
        if Profile.__select_one(self.id) is not None:
            dbs.delete_query("Profiles_Modules", "profiles_id", self.id)
            dbs.delete_query("Profiles", "id", self.id)
            if Profile.__select_one(self.id) is None:
                return 1
            else:
                raise mvc_exc.DeletionError
        else:
            raise mvc_exc.ItemNotExist

    def activate(self, state):
        if Profile.__select_one(self.id) is not None:
            if state is bool:
                self.active = state
                dbs.activate_query("Profiles", state, self.id)
                return 1
            else:
                raise mvc_exc.ParameterUnfilled
        else:
            raise mvc_exc.ItemNotExist

    @staticmethod
    def get_profile(item, name=None):
        if item is not None:
            if name is not None:
                item = Profile.__get_id_by_name(item)
            data = Profile.__select_one(item)
            if data is not None:
                obj_profile = Profile(data[0], data[1], data[2], data[3])
                return obj_profile
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    @staticmethod
    def get_profiles():
        profiles_list = dbs.select_all("Profiles")
        if profiles_list is not None:
            return profiles_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def init(data):
        obj_profile = Profile(data[0], data[1], data[2], data[3])
        return obj_profile

    # """ Database Scripts """
    @staticmethod
    def create():
        sql = """ 
        CREATE TABLE "Profiles" (
        "id" INTEGER NOT NULL,
        "name" TEXT NOT NULL UNIQUE,
        "description" TEXT,
        "active" BOOLEAN DEFAULT 'True',
        PRIMARY KEY("id" AUTOINCREMENT));
        """
        dbs.execute_query(sql)

    @staticmethod
    def __insert(data):
        sql = """ INSERT INTO Profiles (name, description, active) values(?, ?, ?); """
        dbs.execute_query(sql, data)

    @staticmethod
    def __update(data):
        sql = """ UPDATE Profiles SET 
        name= (?), description= (?), active= (?)
        WHERE id == (?) """
        dbs.execute_query(sql, data)

    @staticmethod
    def __get_id_by_name(item):
        result_query = dbs.select_parameter("id", "Profiles", "name", item)
        return result_query

    @staticmethod
    def __select_one(item):
        result_query = dbs.select_one("Profiles", "id", item)
        return result_query
