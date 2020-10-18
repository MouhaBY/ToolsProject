#! /usr/bin/env python3
# coding: utf-8

from src.models import databaseinit as dbi
from src import run


def main():

    """ create database and initialise it by default data """
    dbi.initialise_database()
    """ Running application """
    run.run()


if __name__.endswith('__main__'):
    main()
