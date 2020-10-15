#! /usr/bin/env python3
# coding: utf-8

from models import databaseScripts as dbs


# application definition
def main():
    dbs.initialise_database()


if __name__.endswith('__main__'):
    main()
