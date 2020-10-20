#! /usr/bin/env python3
# coding: utf-8

import src.mvc_exceptions as mvc_exc

from src.models import Pictures_model
from src.models import Companies_model
from src.services import Pictures_services


""" Companies management menu """
""" Show all companies is the default view """


def get_all_companies():
    try:
        companies_list = Companies_model.Company.get_companies()
        # Vue all companies datatable
    except mvc_exc.EmptyList:
        # Vue no element found
        pass


""" User show one company in a new view """


def get_company_by_name(name):
    try:
        company_by_name = Companies_model.Company.get_company(name, "name")
        get_picture_by_id(company_by_name.pictures_id)
        # Vue company details
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue company not found
        pass


# show image related to the  company, this is included in the get company method
def get_picture_by_id(id):
    try:
        picture = Pictures_services.read(id)
        # show image in company details : picture.binary
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue no image found
        pass


# when the user choose to edit or add new picture
def create_new_picture():
    # Defining image storing functions
    filename = ''
    filepath = ''
    binary = ''
    # Creating object and adding it
    new_picture = Pictures_model.Picture.init((None, filename, filepath, binary))
    try:
        new_picture.add()
        return new_picture.id
        # Vue changing photo done
    except mvc_exc.InsertionError:
        # Vue needed to implement
        pass


""" User save new company details and photo affection """


# edit existing company
def edit_company(data):
    company_to_edit = Companies_model.Company.init(data)
    try:
        company_to_edit.edit()
        # Show view of saving data successfully and return to previous view
    except mvc_exc.ItemNotExist:
        # Vue needed to implement, item not found
        pass


""" User delete the company details """


def remove_company(data):
    company_to_remove = Companies_model.Company.init(data)
    try:
        company_to_remove.remove()
        # vue of removing successfully and return to previous view
    except (mvc_exc.ItemNotExist, mvc_exc.DeletionError):
        # Vue needed to implement
        pass


""" user activate or deactivate the company shown """


# deactivate existing company
def deactivate_company(data):
    company_to_deactivate = Companies_model.Company.init(data)
    try:
        company_to_deactivate.activate(0)
        return 1
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue needed to implement
        pass


# activate existing company
def activate_company(data):
    company_to_activate = Companies_model.Company.init(data)
    try:
        company_to_activate.activate(1)
        return 1
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue needed to implement
        pass


""" User add new company """


# Show view of creating company interface

# user saves the data
def create_new_company(data):
    new_company = Companies_model.Company.init(data)
    try:
        new_company.add()
        # show view of saving data successfully
    except mvc_exc.InsertionError:
        # Vue needed to implement
        pass
