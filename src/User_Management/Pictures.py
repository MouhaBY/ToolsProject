#! /usr/bin/env python3
# coding: utf-8

import src.models.Pictures_table as Pictures_table


class Pictures:
    def __init__(self, id, filename, binary, filepath):
        self.filename = filename
        self.binary = binary
        self.filepath = filepath
        self.id = id

    def add(self):
        self.id = Pictures_table.check(self.filename)
        if self.id is None:
            Pictures_table.add((self.filename, self.binary, self.filepath))
            return 1
        else:
            return 0

    def delete(self):
        self.id = Pictures_table.check(self.filename)
        if self.id is not None:
            Pictures_table.delete(self.id)
            return 1
        else:
            return 0

    def edit(self):
        if Pictures_table.check(self.filename) is None:
            if self.id is not None:
                Pictures_table.update((self.filename, self.binary, self.filepath, self.id))
                return 1
            else:
                return 0
        else:
            return 0


def get(item):
    data = Pictures_table.get(item)
    if data is not None:
        _p = Pictures(data[0], data[1], data[2], data[3])
        return _p


def main():
    pass


if __name__.endswith('__main__'):
    main()
