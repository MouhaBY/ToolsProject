#! /usr/bin/env python3
# coding: utf-8


import src.scripts.databasescripts as dbs
import src.common.mvc_exceptions as mvc_exc


class Action:
    def __init__(self, id, name, description, active):
        self.id = id
        self.name = name
        self.description = description
        self.active = active

    def add(self):
        if Action.__get_id_by_name(self.name) is None:
            Action.__insert((self.name, self.description, self.active))
            self.id = Action.__get_id_by_name(self.name)
            if self.id is not None:
                return 1
            else:
                raise mvc_exc.InsertionError
        else:
            raise mvc_exc.ItemAlreadyExist

    def edit(self):
        if self.id is not None:
            if Action.__get_one(self.id) is not None:
                if Action.__get_id_by_name(self.name) is None:
                    Action.__update((self.name, self.description, self.active))
                    return 1
                else:
                    raise mvc_exc.ItemAlreadyExist
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    def remove(self):
        if Action.__get_one(self.id) is not None:
            dbs.delete_query("Actions", "id", self.id)
            if Action.__get_one(self.id) is None:
                return 1
            else:
                raise mvc_exc.DeletionError
        else:
            raise mvc_exc.ItemNotExist

    def activate(self, state):
        if Action.__get_one(self.id) is not None:
            if state is bool:
                self.active = state
                dbs.activate_query("Actions", self.id, state)
                return 1
            else:
                raise mvc_exc.ParameterUnfilled
        else:
            raise mvc_exc.ItemNotExist

    @staticmethod
    def get_action(item, name=None):
        if item is not None:
            if name is not None:
                item = Action.__get_id_by_name(item)
            data = Action.__get_one(item)
            if data is not None:
                obj_action = Action(data[0], data[1], data[2], data[3])
                return obj_action
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    @staticmethod
    def get_actions():
        actions_list = dbs.select_all("Actions")
        if actions_list is not None:
            return actions_list
        else:
            raise mvc_exc.EmptyList

    @staticmethod
    def init(data):
        obj_action = Action(data[0], data[1], data[2], data[3])
        return obj_action

    # """ Database Scripts """
    @staticmethod
    def create():
        sql = """ 
        CREATE TABLE "Actions" (
        "id" INTEGER NOT NULL,
        "name" TEXT NOT NULL UNIQUE,
        "description" TEXT,
        "active" BOOLEAN DEFAULT 'True',
        PRIMARY KEY("id")
        );
        """
        dbs.execute_query(sql)

    @staticmethod
    def __insert(data):
        sql = """ INSERT INTO Actions (name, description, active) values(?, ?, ?); """
        dbs.execute_query(sql, data)

    @staticmethod
    def __update(data):
        sql = """ UPDATE Actions SET 
        name= (?), description= (?), active= (?)
        WHERE id == (?) """
        dbs.execute_query(sql, data)

    @staticmethod
    def __get_id_by_name(item):
        result_query = dbs.select_parameter("id", "Actions", "name", item)
        return result_query

    @staticmethod
    def __get_one(item):
        result_query = dbs.select_one("Actions", "id", item)
        return result_query
