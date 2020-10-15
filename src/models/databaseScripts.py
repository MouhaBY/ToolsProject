#! /usr/bin/env python3
# coding: utf-8

"""creation du fichier de la base des donnees"""

import sqlite3
from sqlite3 import Error

global db_file
db_file = r"..\..\data\database.db"


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def execute_query(query):
    try:
        conn = sqlite3.connect(db_file)
        with conn:
            _result = conn.execute(query)
            conn.commit()
            return _result
        conn.close()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' has occurred")


def execute_query_data(query,data):
    try:
        conn = sqlite3.connect(db_file)
        with conn:
            _result = conn.execute(query, data)
            conn.commit()
            return _result
        conn.close()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' has occurred")


def main():
    create_connection()


if __name__.endswith('__main__'):
    main()