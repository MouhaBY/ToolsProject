#! /usr/bin/env python3
# coding: utf-8

import src.common.mvc_exceptions as mvc_exc

from src.services.Pictures_services import PicturesServices
from src.services.Companies_services import CompaniesServices

""" Companies management menu """
""" Show all companies is the default view """


class CompaniesManagement(object):
    """Class for managing items in the database"""
    def __init__(self):
        self.current_company = None
        self.companies_list = None
        self.current_picture = None
        PicturesServices()
        CompaniesServices()

    def get_all_companies(self):
        try:
            self.companies_list = CompaniesServices.get_companies()
            # Vue all companies datatable
        except:
            # Vue no element found
            self.companies_list = None

    """ User show one company in a new view """

    def get_company(self, id_item):
        try:
            self.current_company = CompaniesServices.read(id_item)
            # Vue company details
        except:
            self.current_company = None
            # Vue company not found

    # when the user choose to edit or add new picture
    def create_new_picture(self):
        # Defining image storing functions
        # with file
        filename = 'name 11'
        filepath = ''
        binary = bytes('example', encoding='utf-8')
        # Creating object and adding it
        try:
            self.current_picture = PicturesServices.create((filename, binary, filepath))
            # Vue changing photo done
        except mvc_exc.InsertionError:
            # Vue needed to implement
            pass

    """ User save new company details and photo affection """

    # edit existing company
    def edit_company(self):
        try:
            self.current_company.name = 'value 1'
            self.current_company.code = 'value 2'
            __edited = CompaniesServices.update(self.current_company)
            self.current_company = __edited
            # Show view of saving data successfully and return to previous view
        except:
            # Vue needed to implement, item not found
            pass

    """ User delete the company details """

    def remove_company(self):
        try:
            self.current_company = CompaniesServices.delete(self.current_company)
            # vue of removing successfully and return to previous view
        except:
            # Vue needed to implement
            pass

    """ user activate or deactivate the company shown """

    # deactivate existing company
    def deactivate_company(self):
        try:
            self.current_company = CompaniesServices.activate(self.current_company, 0)
        except:
            # Vue needed to implement
            pass

    # activate existing company
    def activate_company(self):
        try:
            self.current_company = CompaniesServices.activate(self.current_company, 1)
        except:
            # Vue needed to implement
            pass

    """ User add new company """

    # Show view of creating company interface

    # user saves the data
    def create_new_company(self):
        try:
            company_name = 'name created'
            company_code = 'code created'
            company_active = 1
            company_picture = self.current_picture
            # self.current_company.picture =
            self.current_company = CompaniesServices.create((company_name, company_code, None, None, None
                                                             ,None, None, None, company_picture, company_active))
            # show view of saving data successfully
        except :
            # Vue needed to implement
            pass
