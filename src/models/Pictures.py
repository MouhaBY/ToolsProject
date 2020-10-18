#! /usr/bin/env python3
# coding: utf-8


import src.models.databasescripts as dbs
import src.mvc_exceptions as mvc_exc


class Picture:
    def __init__(self, id, filename, binary, filepath):
        self.id = id
        self.filename = filename
        self.binary = binary
        self.filepath = filepath

    def add(self):
        self.id = Picture.__insert((self.filename, self.binary, self.filepath))
        if self.id is not None:
            return 1
        else:
            raise mvc_exc.InsertionError

    def remove(self):
        data = Picture.__select(self.id)
        if data is not None:
            dbs.delete_query("Pictures", "id", self.id)
            if Picture.__select(self.id) is None:
                return 1
            else:
                raise mvc_exc.DeletionError
        else:
            raise mvc_exc.ItemNotExist

    # STATIC PUBLIC METHODS
    @staticmethod
    def init(data):
        obj_picture = Picture(data[0], data[1], data[2], data[3])
        return obj_picture

    @staticmethod
    def get(item):
        if item is not None:
            data = Picture.__select(item)
            if data is not None:
                obj_picture = Picture(data[0], data[1], data[2], data[3])
                return obj_picture
            else:
                raise mvc_exc.ItemNotExist
        else:
            raise mvc_exc.ParameterUnfilled

    @staticmethod
    def create():
        sql = """ 
        CREATE TABLE "Pictures" (
        "id" INTEGER NOT NULL,
        "filename" TEXT,
        "binary" BLOB,
        "filepath"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
        );
        """
        dbs.execute_query(sql)

    # """ Database specific scripts """
    @staticmethod
    def __insert(data):
        sql = """ INSERT INTO Pictures (filename, binary, filepath) values(?, ?, ?); """
        dbs.execute_query(sql, data)
        # return id value of inserted row
        sql_2 = """ SELECT MAX(id) FROM Pictures """
        _result = dbs.execute_query(sql_2)
        try:
            return _result.fetchone()[0]
        except TypeError:
            return None

    @staticmethod
    def __select(item):
        result_query = dbs.select_one("Pictures", "id", item)
        return result_query
