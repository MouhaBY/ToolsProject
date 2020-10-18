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
import src.models.Actions_table as Actions_table
import src.models.ActivityLog_table as ActivityLog_table


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
    Actions_table.create()
    ActivityLog_table.create()