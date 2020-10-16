#! /usr/bin/env python3
# coding: utf-8

import src.models.databaseScripts as dbs

import src.models.Contacts_table as Contacts_table
import src.models.Companies_table as Companies_table
import src.models.Users_table as Users_table
import src.models.Pictures_table as Pictures_table

def initialise_database():

    # Create database
    dbs.create_connection()

    # Create Tables
    Pictures_table.create()
    Companies_table.create()
    Contacts_table.create()
    Users_table.create()

    # Create default data
    Pictures_table.add(("filename", "0XDHFRE", "C:"))
    Companies_table.add(("Company", "Comp-001", "Tunisia", "TVA01", "00216phone", "00216mobile", "www.company.com", "contact@company.com", 1))
    Contacts_table.add(("Mohammed", "BEN YAHIA", "Tunisia", "Matricule01", "00216phone", "00216mobile", "1", "Engineer", 1))
    Users_table.add(("MBY", "123", "mohammed.beny@hotmail.fr", "1", 1))
