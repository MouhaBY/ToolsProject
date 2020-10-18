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
        if get_id("username", self.username) is None:
            if get_id("email", self.email) is None:
                insert((self.username, self.password, self.email, self.contact_id, self.active))
                self.id = get_id("username", self.username)
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
            if get_one(self.id) is not None:
                update((self.username, self.password, self.email, self.contact_id, self.active, self.id))
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
    def get_user(item, username=None):
        if item is not None:
            if username is not None:
                item = get_id("username", item)
            data = get_one(item)
            if data is not None:
                obj_user = User(data[0], data[1], data[2], data[3], data[4], data[5])
                return obj_user
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    @staticmethod
    def get_users():
        users_list = get_all()
        if users_list is not None:
            return users_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def init(data):
        obj_user = User(data[0], data[1], data[2], data[3], data[4], data[5])
        return obj_user


""" database scripts """


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


def insert(data):
    sql = """ INSERT INTO Users (username, password, email, contact_id, active)
                    values(?, ?, ?, ?, ?) """
    dbs.execute_query(sql, data)


def update(data):
    sql = """ UPDATE Users SET 
    username= (?), password= (?), email= (?), contact_id= (?), active= (?)
    WHERE id == (?) """
    dbs.execute_query(sql, data)


def delete(item):
    dbs.delete_query("Users", "id", item)


def get_id(reference, item):
    result_query = dbs.select_parameter("id", "Users", reference, item)
    return result_query


def get_one(item):
    result_query = dbs.select_one("Users", "id", item)
    return result_query


def get_all():
    result_query = dbs.select_all("Users")
    return result_query


def activate_sql(data):
    dbs.activate_query("Users", data[0], data[1])
