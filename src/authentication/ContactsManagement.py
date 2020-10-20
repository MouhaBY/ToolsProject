#! /usr/bin/env python3
# coding: utf-8

import src.mvc_exceptions as mvc_exc

from src.models import Pictures_model
from src.models import Contacts


""" Contacts management menu """
""" Show all contacts is the default view """


def get_all_contacts():
    try:
        contacts_list = Contacts.Contact.get_contacts()
        # Vue all contacts datatable
    except mvc_exc.EmptyList:
        # Vue no element found
        pass


""" User show one contact in a new view """


def get_contact_by_id(id):
    try:
        contact_by_id = Contacts.Contact.get_contact(id)
        get_picture_by_id(contact_by_id.pictures_id)
        # Vue company details
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue company not found
        pass


# show image related to the  company, this is included in the get contact method
def get_picture_by_id(item):
    try:
        picture_by_id = Pictures_model.Picture.get(item)
        # show image in contact details
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue no image found
        pass


# Convert digital data to binary format
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data


# when the user choose to edit or add new picture
def create_new_picture():
    # Defining image storing functions
    filename = ''
    binary = convertToBinaryData(filename)
    # Creating object and adding it
    new_picture = Pictures_model.Picture.init((None, None, None, binary))
    try:
        new_picture.add()
        return new_picture.id
        # Vue changing photo done
    except mvc_exc.InsertionError:
        # Vue needed to implement
        pass


""" User save new contact details and photo affection """


# edit existing contact
def edit_contact(data):
    contact_to_edit = Contacts.Contact.init(data)
    try:
        contact_to_edit.edit()
        # Show view of saving data successfully and return to previous view
    except mvc_exc.ItemNotExist:
        # Vue needed to implement, item not found
        pass


""" User delete the contact details """


def remove_contact(data):
    contact_to_remove = Contacts.Contact.init(data)
    try:
        contact_to_remove.remove()
        # vue of removing successfully and return to previous view
    except (mvc_exc.ItemNotExist, mvc_exc.DeletionError):
        # Vue needed to implement
        pass


""" user activate or deactivate the contact shown """


# deactivate existing company
def deactivate_contact(data):
    contact_to_deactivate = Contacts.Contact.init(data)
    try:
        contact_to_deactivate.activate(0)
        return 1
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue needed to implement
        pass


# activate existing company
def activate_contact(data):
    contact_to_activate = Contacts.Contact.init(data)
    try:
        contact_to_activate.activate(1)
        return 1
    except (mvc_exc.ItemNotExist, mvc_exc.ParameterUnfilled):
        # Vue needed to implement
        pass


""" User add new contact """


# Show view of creating company interface

# user saves the data
def create_new_contact(data):
    new_contact = Contacts.Contact.init(data)
    try:
        new_contact.add()
        # show view of saving data successfully
    except mvc_exc.InsertionError:
        # Vue needed to implement
        pass
