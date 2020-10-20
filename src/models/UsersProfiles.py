#! /usr/bin/env python3
# coding: utf-8


import src.scripts.databasescripts as dbs
import src.mvc_exceptions as mvc_exc


class UserProfile:
    def __init__(self, users_id, profiles_id):
        self.users_id = users_id
        self.profiles_id = profiles_id

    def add(self):
        if UserProfile.__select_one((self.users_id, self.profiles_id)) is None:
            UserProfile.__insert((self.users_id, self.profiles_id))
            if UserProfile.__select_one((self.users_id, self.profiles_id)) is not None:
                return 1
            else:
                raise mvc_exc.InsertionError
        else:
            raise mvc_exc.ItemAlreadyExist

    def remove(self):
        if UserProfile.__select_one((self.users_id, self.profiles_id)) is not None:
            dbs.delete_two_conditions("Profiles_Modules", "users_id", self.users_id, "profiles_id", self.profiles_id)
            if UserProfile.__select_one((self.users_id, self.profiles_id)) is None:
                return 1
            else:
                raise mvc_exc.DeletionError
        else:
            raise mvc_exc.ItemAlreadyExist

    @staticmethod
    def get_users_profiles():
        users_profiles_list = dbs.select_all("Users_Profiles")
        if users_profiles_list is not None:
            return users_profiles_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def get_user_profiles(user_id):
        user_profiles_list = dbs.select_list("Users_Profiles", "users_id", user_id)
        if user_profiles_list is not None:
            return user_profiles_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def init(data):
        obj_user_profile = UserProfile(data[0], data[1])
        return obj_user_profile

    # """ Database Scripts """
    @staticmethod
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

    @staticmethod
    def __insert(data):
        sql = """ INSERT INTO Users_Profiles (users_id, profiles_id) values(?, ?); """
        dbs.execute_query(sql, data)

    @staticmethod
    def __select_one(data):
        result_query = dbs.select_two_conditions("Users_Profiles", "users_id", data[0], "profiles_id", data[1])
        return result_query
