#! /usr/bin/env python3
# coding: utf-8

import src.models.Pictures_table as Pictures_table


class Picture:
    def __init__(self, id, filename, binary, filepath):
        self.id = id
        self.filename = filename
        self.binary = binary
        self.filepath = filepath

    def add(self):
        self.id = Pictures_table.add((self.filename, self.binary, self.filepath))
        if self.id is not None:
            return 1

    def delete(self):
        data = Pictures_table.read(self.id)
        if data is not None:
            Pictures_table.delete(self.id)
            return 1


def get(item):
    data = Pictures_table.read(item)
    if data is not None:
        obj_picture = Picture(data[0], data[1], data[2], data[3])
        return obj_picture


def init(data):
    obj_picture = Picture(data[0], data[1], data[2], data[3])
    return obj_picture
