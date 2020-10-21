#! /usr/bin/env python3
# coding: utf-8


class ItemNotExist(Exception):
    pass


class EmptyList(Exception):
    pass


class ItemAlreadyExist(Exception):
    pass


class InsertionError(Exception):
    pass


class DeletionError(Exception):
    pass


class UpdateError(Exception):
    pass


class ParameterUnfilled(Exception):
    pass
