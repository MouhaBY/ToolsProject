#! /usr/bin/env python3
# coding: utf-8

class StandardView(object):
    def __init(self):
        self.object_name = None

    @staticmethod
    def show_notfound_error():
        print('element not found')

    @staticmethod
    def show_emptylist():
        print('liste vide')

    @staticmethod
    def saved_successfully():
        print('enregistrement effectué')

    @staticmethod
    def not_saved():
        print('enregistrement échoué')

    @staticmethod
    def already_exists():
        print('element déja existant')

    @staticmethod
    def deleted_successfully():
        print('suppression effectué')

    @staticmethod
    def not_deleted():
        print('suppression echouée')
