#! /usr/bin/env python3
# coding: utf-8

import src.models.Contacts as Contacts_table
import src.models.Companies as Companies_table
import src.models.Users as Users_table
from src.models import Pictures_model
import src.models.Profiles as Profiles_table
import src.models.UsersProfiles as UsersProfiles_Table
import src.models.Modules as Modules_table
import src.models.ProfilesModules as ProfilesModules_table
import src.models.Actions as Actions_table
import src.models.ActivityLog as ActivityLog_table


def initialise_database(engine):
    # Create database
    # Create Tables
    Pictures_model.Base.metadata.create_all(engine)
