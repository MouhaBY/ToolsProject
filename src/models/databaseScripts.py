#! /usr/bin/env python3
# coding: utf-8


import sqlite3
from sqlite3 import Error


# database file directory
global db_file
db_file = r".\data\database.db"


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


def select_parameter(parameter, table_name, reference, item):
    sql = 'SELECT {} FROM {} WHERE {} == "{}"'.format(parameter, table_name, reference, item)
    _result = execute_query(sql)
    try:
        return _result.fetchone()[0]
    except TypeError:
        return None


def select_one(table_name, reference, item):
    sql = 'SELECT * FROM {} WHERE {} == "{}"'.format(table_name, reference, item)
    _result = execute_query(sql)
    try:
        return _result.fetchone()
    except TypeError:
        return None


def select_list(table_name, reference, item):
    sql = 'SELECT * FROM {} WHERE {} == "{}"'.format(table_name, reference, item)
    _result = execute_query(sql)
    try:
        return _result.fetchall()
    except TypeError:
        return None


def select_all(table_name):
    sql = 'SELECT * FROM {}'.format(table_name)
    _result = execute_query(sql)
    try:
        return _result.fetchall()
    except TypeError:
        return None


def delete_query(table_name, reference, item):
    sql = 'DELETE FROM {} WHERE {} = "{}"'.format(table_name, reference, item)
    execute_query(sql)


def activate_query(table_name, item, value):
    sql = 'UPDATE {} SET active = {} WHERE id == "{}"'.format(table_name, value, item)
    execute_query(sql)


def main():
    pass


if __name__.endswith('__main__'):
    main()
