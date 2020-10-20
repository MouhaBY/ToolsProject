#! /usr/bin/env python3
# coding: utf-8

from src import databaseinit as dbi
import config


def main():
    """ create database and tables """
    dbi.initialise_database(config.engine)
    print("application is running")


if __name__.endswith('__main__'):
    main()
