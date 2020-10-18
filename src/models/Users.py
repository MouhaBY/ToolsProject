#! /usr/bin/env python3
# coding: utf-8


import src.models.databasescripts as dbs
import src.mvc_exceptions as mvc_exc


class User:
    def __init__(self, id, username, password, email, contact_id, active):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.contact_id = contact_id
        self.active = active

    def add(self):
        if User.__get_id_by_reference("username", self.username) is None:
            if User.__get_id_by_reference("email", self.email) is None:
                User.__insert((self.username, self.password, self.email, self.contact_id, self.active))
                self.id = User.__get_id_by_reference("username", self.username)
                if self.id is not None:
                    return 1
                else:
                    raise mvc_exc.InsertionError
            else:
                raise mvc_exc.ItemAlreadyExist
        else:
            raise mvc_exc.ItemAlreadyExist

    def edit(self):
        if self.id is not None:
            if User.__select_one(self.id) is not None:
                User.__update((self.username, self.password, self.email, self.contact_id, self.active, self.id))
                return 1
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    def remove(self):
        if User.__select_one(self.id) is not None:
            dbs.delete_query("Users_Profiles", "users_id", self.id)
            dbs.delete_query("Users", "id", self.id)
            if User.__select_one(self.id) is None:
                return 1
            else:
                raise mvc_exc.DeletionError
        else:
            raise mvc_exc.ItemNotExist

    def activate(self, state):
        if User.__select_one(self.id) is not None:
            if state is bool:
                self.active = state
                dbs.activate_query("Users", state, self.id)
                return 1
            else:
                raise mvc_exc.ParameterUnfilled
        else:
            raise mvc_exc.ItemNotExist

    @staticmethod
    def get_user(item, username=None):
        if item is not None:
            if username is not None:
                item = User.__get_id_by_reference("username", item)
            data = User.__select_one(item)
            if data is not None:
                obj_user = User(data[0], data[1], data[2], data[3], data[4], data[5])
                return obj_user
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    @staticmethod
    def get_users():
        users_list = dbs.select_all("Users")
        if users_list is not None:
            return users_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def init(data):
        obj_user = User(data[0], data[1], data[2], data[3], data[4], data[5])
        return obj_user

    # """ database scripts """
    @staticmethod
    def create():
        sql = """ 
        CREATE TABLE "Users" (
        "id" INTEGER NOT NULL,
        "username" TEXT NOT NULL UNIQUE,
        "password" TEXT NOT NULL,
        "email" TEXT,
        "contact_id" INTEGER,
        "active" BOOLEAN DEFAULT 'True',
        FOREIGN KEY("contact_id") REFERENCES "Contacts"("id"),
        PRIMARY KEY("id" AUTOINCREMENT)
        );
        """
        dbs.execute_query(sql)

    @staticmethod
    def __insert(data):
        sql = """ INSERT INTO Users (username, password, email, contact_id, active)
                        values(?, ?, ?, ?, ?) """
        dbs.execute_query(sql, data)

    @staticmethod
    def __update(data):
        sql = """ UPDATE Users SET 
        username= (?), password= (?), email= (?), contact_id= (?), active= (?)
        WHERE id == (?) """
        dbs.execute_query(sql, data)

    @staticmethod
    def __get_id_by_reference(reference, item):
        result_query = dbs.select_parameter("id", "Users", reference, item)
        return result_query

    @staticmethod
    def __select_one(item):
        result_query = dbs.select_one("Users", "id", item)
        return result_query
