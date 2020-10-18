#! /usr/bin/env python3
# coding: utf-8

import src.mvc_exceptions as mvc_exc

from src.models import Pictures
from src.models import Companies


""" Pictures management to add into database 
from contacts or companies and reading picture from database """


# Pictures manipulating
def get_picture_by_id(item):
    try:
        picture_by_id = Pictures.get(item)
        return picture_by_id
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue needed to implement
        pass


def create_new_picture():
    # Defining image storing functions
    filename = ''
    filepath = ''
    binary = ''
    # Creating object and adding it
    new_picture = Pictures.init((None, filename, filepath, binary))
    try:
        new_picture.add()
        return new_picture.id
    except mvc_exc.InsertionError:
        # Vue needed to implement
        pass


""" Companies management to add into database 
from contacts or companies and reading companies from database """


# Companies Manipulating
def get_all_companies():
    try:
        companies_list = Companies.get_companies()
        return companies_list
    except mvc_exc.EmptyList:
        # Vue needed to implement
        pass


# """ Contacts management interface """
def get_company_by_id(id):
    try:
        company_by_id = Companies.get_company(id)
        return company_by_id
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue needed to implement
        pass


# """ Companies management interface """
def get_company_by_name(name):
    try:
        company_by_name = Companies.get_company(name, "name")
        return company_by_name
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue needed to implement
        pass


# """ create new company """
def create_new_company(data):
    new_company = Companies.init(data)
    try:
        new_company.add()
        return new_company.id
    except mvc_exc.InsertionError:
        # Vue needed to implement
        pass


# edit existing company
def edit_company(data):
    company_to_edit = Companies.init(data)
    try:
        company_to_edit.edit()
        return company_to_edit.id
    except mvc_exc.ItemNotExist:
        # Vue needed to implement
        pass


# remove existing company
def remove_company(data):
    company_to_remove = Companies.init(data)
    try:
        company_to_remove.remove()
        return 1
    except (mvc_exc.ItemNotExist, mvc_exc.DeletionError):
        # Vue needed to implement
        pass


# deactivate existing company
def deactivate_company(data):
    company_to_deactivate = Companies.init(data)
    try:
        company_to_deactivate.activate(0)
        return 1
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue needed to implement
        pass


# activate existing company
def activate_company(data):
    company_to_deactivate = Companies.init(data)
    try:
        company_to_deactivate.activate(1)
        return 1
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue needed to implement
        pass
