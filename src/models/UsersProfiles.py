#! /usr/bin/env python3
# coding: utf-8


import src.models.databasescripts as dbs
import src.mvc_exceptions as mvc_exc


class UserProfile:
    def __init__(self, users_id, profiles_id):
        self.users_id = users_id
        self.profiles_id = profiles_id

    def add(self):
        if get_one((self.users_id, self.profiles_id)) is None:
            insert((self.users_id, self.profiles_id))
            if get_one((self.users_id, self.profiles_id)) is not None:
                return 1
            else:
                raise mvc_exc.InsertionError
        else:
            raise mvc_exc.ItemAlreadyExist

    def remove(self):
        if get_one((self.users_id, self.profiles_id)) is not None:
            delete((self.users_id, self.profiles_id))
            if get_one((self.users_id, self.profiles_id)) is None:
                return 1
            else:
                raise mvc_exc.DeletionError
        else:
            raise mvc_exc.ItemAlreadyExist

    @staticmethod
    def get_users_profiles():
        users_profiles_list = get_all()
        if users_profiles_list is not None:
            return users_profiles_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def get_user_profiles(user_id):
        user_profiles_list = get_list(user_id)
        if user_profiles_list is not None:
            return user_profiles_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def init(data):
        obj_user_profile = UserProfile(data[0], data[1])
        return obj_user_profile


""" Database Scripts """


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


def insert(data):
    sql = """ INSERT INTO Users_Profiles (users_id, profiles_id) values(?, ?); """
    dbs.execute_query(sql, data)


def delete(data):
    dbs.delete_two_conditions("Profiles_Modules","profiles_id", data[0], "modules_id", data[1])


def get_one(data):
    result_query = dbs.select_two_conditions("Users_Profiles", "users_id", data[0], "profiles_id", data[1])
    return result_query


def get_all():
    result_query = dbs.select_all("Users_Profiles")
    return result_query


def get_list(item):
    result_query = dbs.select_list("Users_Profiles", "users_id", item)
    return result_query
