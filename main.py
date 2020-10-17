#! /usr/bin/env python3
# coding: utf-8

from src import databaseInit as dbi


def main():

    """ create database and initialise it by default data """
    dbi.initialise_database()


if __name__.endswith('__main__'):
    main()
