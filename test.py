#! /usr/bin/env python3
# coding: utf-8

from src.authentication import authentication


picture_id = authentication.create_new_picture()

if picture_id is not None:
    print('OK')
else:
    print('NOK')

if authentication.get_picture_by_id(picture_id) is not None:
    print('OK')
else:
    print('NOK')

if authentication.get_all_companies() is not None:
    print('OK')
else:
    print('NOK')

if authentication.get_company_by_id("1") is not None:
    print('OK')
else:
    print('NOK')

if authentication.get_company_by_name("Company") is not None:
    print('OK 5')
else:
    print('NOK 5')

new_company_id = authentication.create_new_company(("Companytested11", "Comp-001", "Tunisia", "TVA01", "00216phone",
                                      "00216mobile", "www.company.com", "contact@company.com", None, 1))
if new_company_id is not None:
    print('OK')
else:
    print('NOK')

company_to_edit_id = authentication.edit_company(("Companytested1", "Comp-0011", "Tunisia", "TVA01", "00216phone",
                                      "00216mobile", "www.company.com", "contact@company.com", None, 1))

if company_to_edit_id is not None:
    print('OK')
else:
    print('NOK')








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
