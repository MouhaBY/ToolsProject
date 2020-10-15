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


def execute_query(query, data=None):
    try:
        conn = sqlite3.connect(db_file)
        with conn:
            if data is None:
                _result = conn.execute(query)
                conn.commit()
            else:
                _result = conn.execute(query, data)
                conn.commit()
        return _result
        conn.close()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' has occurred")


def select_query(table_name, data="all", reference=None, item=None):
    if item is None:
        sql = 'SELECT * FROM {}'.format(table_name)
    else:
        sql = 'SELECT * FROM {} WHERE {} = "{}"'.format(table_name, reference, item)
    _result = execute_query(sql)
    if data == "all":
        result_query = _result.fetchall()
    elif data == "row":
        result_query = _result.fetchone()
    else:
        result_query = None
    return result_query


def delete_query(table_name, reference, item):
    sql = 'DELETE FROM {} WHERE {} = "{}"'.format(table_name, reference, item)
    _result = execute_query(sql)
    result_query = _result.fetchone()
    return result_query


def main():
    create_connection()


if __name__.endswith('__main__'):
    main()