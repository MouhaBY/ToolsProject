#! /usr/bin/env python3
# coding: utf-8

from src.authentication import CompaniesManagement


CompaniesManagement.create_new_picture(company)

if picture_id is not None:
    print('OK')
else:
    print('NOK')

if CompaniesManagement.get_picture_by_id(picture_id) is not None:
    print('OK')
else:
    print('NOK')

if CompaniesManagement.get_all_companies() is not None:
    print('OK')
else:
    print('NOK')

if CompaniesManagement.get_company_by_name("Company") is not None:
    print('OK ')
else:
    print('NOK ')

new_company_id = CompaniesManagement.create_new_company((None, "Companytested11111d25", "Comp-001", "Tunisia", "TVA01", "00216phone",
                                                    "00216mobile", "www.company.com", "contact@company.com", None, 1))
if new_company_id is not None:
    print('OK')
else:
    print('NOK')

company_to_edit_id = CompaniesManagement.edit_company((new_company_id, "Companytestedd255", "Comp-0011", "Tunisia", "TVA01", "00216phone",
                                      "00216mobile", "www.company.com", "contact@company.com", None, 1))

if company_to_edit_id is not None:
    print('OK')
else:
    print('NOK')

company_to_deactivate = CompaniesManagement.deactivate_company((new_company_id, "Companytested1", "Comp-0011", "Tunisia", "TVA01", "00216phone",
                                                            "00216mobile", "www.company.com", "contact@company.com", None, 1))

if company_to_deactivate is not None:
    print('OK')
else:
    print('NOK')

company_to_remove = CompaniesManagement.remove_company((new_company_id, "Companytested1", "Comp-0011", "Tunisia", "TVA01",
                                                   "00216phone", "00216mobile", "www.company.com", "contact@company.com", None,
                                                        1))

if company_to_remove is not None:
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
