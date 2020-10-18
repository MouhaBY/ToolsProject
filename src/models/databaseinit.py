#! /usr/bin/env python3
# coding: utf-8

import src.models.databasescripts as dbs

import src.models.Contacts as Contacts_table
import src.models.Companies as Companies_table
import src.models.Users as Users_table
import src.models.Pictures as Pictures
import src.models.Profiles as Profiles_table
import src.models.UsersProfiles as UsersProfiles_Table
import src.models.Modules as Modules_table
import src.models.ProfilesModules as ProfilesModules_table
import src.models.Actions as Actions_table
import src.models.ActivityLog as ActivityLog_table


def initialise_database():

    # Create database
    dbs.create_connection()

    # Create Tables
    Pictures.Picture.create()
    Companies_table.Company.create()
    Contacts_table.Contact.create()
    Users_table.User.create()
    Profiles_table.Profile.create()
    UsersProfiles_Table.UserProfile.create()
    Modules_table.Module.create()
    ProfilesModules_table.ProfileModule.create()
    Actions_table.Action.create()
    ActivityLog_table.ActivityLog.create()
