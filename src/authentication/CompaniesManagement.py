#! /usr/bin/env python3
# coding: utf-8

import src.common.mvc_exceptions as mvc_exc

from src.services.Pictures_services import PicturesServices
from src.services.Companies_services import CompaniesServices

from src.ui.CompaniesView import CompaniesView
from src.ui.CompanyView import CompanyView
from src.ui.StandardViews import StandardView

""" Companies management menu """
""" Show all companies is the default view """


class CompaniesManagement(object):
    """Class for managing items in the database"""
    def __init__(self):
        self.picture_service = PicturesServices()
        self.company_service = CompaniesServices()
        self.companies_view = CompaniesView()
        self.company_view = CompanyView()
        self.standard_view = StandardView()

    def get_all_companies(self):
        # get data from database to datalist objects
        __companies_list = self.company_service.get_companies_objects()
        # vue afficher toute la liste
        if __companies_list is not None:
            companies_list_dict = self.company_service.get_companies_details()
            self.companies_view.show_companieslist(companies_list_dict)
        else:
            self.standard_view.show_emptylist()

    """ User show one company in a new view """

    def get_company(self):
        # retrieve id item from vue
        id_item = "2"
        try:
            __obj_to_show = self.company_service.get_company_object(id_item)
            __obj_to_show_data = self.company_service.get_company_details()
            # Vue company details
            self.company_view.show_company_details(__obj_to_show_data)
        except mvc_exc.ItemNotExist:
            # Vue company not found
            self.standard_view.show_notfound_error()

    # when the user choose to edit or add new picture
    def create_new_picture(self):
        # path from view
        image_filepath = "D:/logo.png"
        # Read Image
        try:
            __picture_created = self.picture_service.create(image_filepath)
            self.company_service.current_company.picture = __picture_created
            # Vue charging photo done
            self.standard_view.saved_successfully()
        except mvc_exc.InsertionError:
            # Vue needed to implement
            self.standard_view.not_saved()

    """ User save new company details and photo affection """

    # edit existing company
    def edit_company(self):
        try:
            # datas from view
            self.company_service.current_company.code = 'value_1'
            self.company_service.current_company.name = 'value_2'
            self.company_service.update()
            # Show view of saving data successfully and return to previous view
            self.standard_view.saved_successfully()
        except mvc_exc.ItemAlreadyExist:
            self.standard_view.already_exists()

    # edit picture for existing company
    def edit_company_picture(self):
        pass

    """ User delete the company details """

    def remove_company(self):
        try:
            self.company_service.delete()
            # vue of removing successfully and return to previous view
            self.standard_view.deleted_successfully()
        except mvc_exc.DeletionError:
            self.standard_view.not_deleted()

    """ user activate or deactivate the company shown """

    # deactivate existing company
    def deactivate_company(self):
        try:
            self.company_service.activate(0)
            self.standard_view.saved_successfully()
        except:
            self.standard_view.not_saved()

    # activate existing company
    def activate_company(self):
        try:
            self.company_service.activate(1)
            self.standard_view.saved_successfully()
        except:
            self.standard_view.not_saved()

    """ User add new company """

    # Show view of creating company interface

    # user saves the data
    def create_new_company(self):
        try:
            self.company_service.init_company()
            self.company_service.current_company.name = 'name created_'
            self.company_service.current_company.code = 'code created'
            self.company_service.current_company.active = 1
            self.company_service.create()
            self.standard_view.saved_successfully()
        except mvc_exc.ItemAlreadyExist:
            self.standard_view.saved_successfully()
