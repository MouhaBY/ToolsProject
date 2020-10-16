#! /usr/bin/env python3
# coding: utf-8

from src import databaseInit as dbi


# application definition
def main():
    dbi.initialise_database()


if __name__.endswith('__main__'):
    main()
