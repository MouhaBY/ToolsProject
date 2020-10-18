#! /usr/bin/env python3
# coding: utf-8

import src.models.databasescripts as dbs

import src.models.Contacts as Contacts_table
import src.models.Companies as Companies_table
import src.models.Users as Users_table
import src.models.Pictures as Pictures
import src.models.Profiles as Profiles_table
import src.models.UsersProfiles_table as UsersProfiles_Table
import src.models.Modules as Modules_table
import src.models.ProfilesModules_table as ProfilesModules_table
import src.models.Actions as Actions_table
import src.models.ActivityLog as ActivityLog_table


def initialise_database():

    # Create database
    dbs.create_connection()

    # Create Tables
    Pictures.create()
    Companies_table.create()
    Contacts_table.create()
    Users_table.create()
    Profiles_table.create()
    UsersProfiles_Table.create()
    Modules_table.create()
    ProfilesModules_table.create()
    Actions_table.create()
    ActivityLog_table.create()
