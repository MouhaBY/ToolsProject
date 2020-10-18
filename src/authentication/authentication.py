#! /usr/bin/env python3
# coding: utf-8

import src.mvc_exceptions as mvc_exc

from src.models import Pictures
from src.models import Companies


""" Pictures management to add into database 
from contacts or companies and reading pictures from database """


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
    new_picture = Pictures.init((filename, filepath, binary))
    try:
        new_picture.add()
        return new_picture.id
    except mvc_exc.InsertionError:
        # Vue needed to implement
        pass


# Companies Manipulating
def get_all_companies():
    try:
        companies_list = Companies.get_companies()
        return companies_list
    except mvc_exc.EmptyList:
        # Vue needed to implement
        pass


# """ Contacts management interface """
def get_company_by_id(item):
    try:
        company_by_id = Companies.get_company(item)
        return company_by_id
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue needed to implement
        pass


# """ Companies management interface """
def get_company_by_name(item):
    try:
        company_by_name = Companies.get_company(item, "name")
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
