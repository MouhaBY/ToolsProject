#! /usr/bin/env python3
# coding: utf-8


import src.models.databasescripts as dbs
import src.mvc_exceptions as mvc_exc


class ProfileModule:
    def __init__(self, profiles_id, modules_id):
        self.profiles_id = profiles_id
        self.modules_id = modules_id

    def add(self):
        if ProfileModule.__select_one((self.profiles_id, self.modules_id)) is None:
            ProfileModule.__insert((self.profiles_id, self.modules_id))
            if ProfileModule.__select_one((self.profiles_id, self.modules_id)) is not None:
                return 1
            else:
                raise mvc_exc.InsertionError
        else:
            raise mvc_exc.ItemAlreadyExist

    def remove(self):
        if ProfileModule.__select_one((self.profiles_id, self.modules_id)) is not None:
            dbs.delete_two_conditions("Profiles_Modules", "profiles_id", self.profiles_id,
                                      "modules_id", self.modules_id)
            if ProfileModule.__select_one((self.profiles_id, self.modules_id)) is None:
                return 1
            else:
                raise mvc_exc.DeletionError
        else:
            raise mvc_exc.ItemAlreadyExist

    @staticmethod
    def get_profiles_modules():
        profiles_modules_list = dbs.select_all("Profiles_Modules")
        if profiles_modules_list is not None:
            return profiles_modules_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def get_profile_modules(profile_id):
        profile_modules_list = dbs.select_list("Profiles_Modules", "profiles_id", profile_id)
        if profile_modules_list is not None:
            return profile_modules_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def init(data):
        obj_profile_module = ProfileModule(data[0], data[1])
        return obj_profile_module

    # """ Database Scripts """
    @staticmethod
    def create():
        sql = """
        CREATE TABLE "Profiles_Modules" (
        "profiles_id" INTEGER NOT NULL,
        "modules_id" INTEGER NOT NULL,
        FOREIGN KEY("modules_id") REFERENCES "Modules"("id"),
        PRIMARY KEY("profiles_id","modules_id"),
        FOREIGN KEY("profiles_id") REFERENCES "Profiles"("id")
        );
        """
        dbs.execute_query(sql)

    @staticmethod
    def __insert(data):
        sql = """ INSERT INTO Profiles_Modules (profiles_id, modules_id) values(?, ?); """
        dbs.execute_query(sql, data)

    @staticmethod
    def __select_one(data):
        result_query = dbs.select_two_conditions("Profiles_Modules", "profiles_id", data[0], "modules_id", data[1])
        return result_query
