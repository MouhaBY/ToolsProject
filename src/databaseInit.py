#! /usr/bin/env python3
# coding: utf-8

import src.models.databaseScripts as dbs

import src.models.Contacts_table as Contacts_table
import src.models.Companies_table as Companies_table
import src.models.Users_table as Users_table
import src.models.Pictures_table as Pictures_table
import src.models.Profiles_table as Profiles_table
import src.models.UsersProfiles_table as UsersProfiles_Table
import src.models.Modules_table as Modules_table
import src.models.ProfilesModules_table as ProfilesModules_table


def initialise_database():

    # Create database
    dbs.create_connection()

    # Create Tables
    Pictures_table.create()
    Companies_table.create()
    Contacts_table.create()
    Users_table.create()
    Profiles_table.create()
    UsersProfiles_Table.create()
    Modules_table.create()
    ProfilesModules_table.create()

    # Create default data
    Pictures_table.add(("filename", "0XDHFRE", "C:"))
    Companies_table.add(("Company", "Comp-001", "Tunisia", "TVA01", "00216phone", "00216mobile", "www.company.com", "contact@company.com", None, 1))
    Contacts_table.add(("Mohammed", "BEN YAHIA", "Tunisia", "Matricule01", "00216phone", "00216mobile", "1", "Engineer",None, 1))
    Users_table.add(("MBY", "123", "mohammed.beny@hotmail.fr", "1", 1))
    Profiles_table.add(("Profile", "description", 1))
    UsersProfiles_Table.affect(("1","1"))
    Modules_table.add(("Module", "description", 1))
    ProfilesModules_table.affect(("1", "1"))
