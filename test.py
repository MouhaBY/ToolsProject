#! /usr/bin/env python3
# coding: utf-8

from src.authentication import Pictures

# create obj picture
P = Pictures.init((None,'Image1',"Oxd",None))
if P.id is None:
    print("OK 1/4")
result = P.delete()
if result is None:
    print("OK 2/4")
P.add()
if P.id is not None:
    print("OK 3/4")
result = P.delete()
if result ==1:
    print("OK 4/4")




# Create default data

# Pictures_table.add(("filename", "0XDHFRE", "C:"))
# Companies_table.add(("Company", "Comp-001", "Tunisia", "TVA01", "00216phone", "00216mobile", "www.company.com", "contact@company.com", None, 1))
# Contacts_table.add(("Mohammed", "BEN YAHIA", "Tunisia", "Matricule01", "00216phone", "00216mobile", "1", "Engineer",None, 1))
# Users_table.add(("MBY", "123", "mohammed.beny@hotmail.fr", "1", 1))
# Profiles_table.add(("Profile", "description", 1))
# UsersProfiles_Table.affect(("1","1"))
# Modules_table.add(("Module", "description", 1))
# ProfilesModules_table.affect(("1", "1"))
# Actions_table.add(("action1", "description", 1))
