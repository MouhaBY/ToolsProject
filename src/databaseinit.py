#! /usr/bin/env python3
# coding: utf-8

from src.models import Pictures_model
from src.models import Companies_model


def initialise_database(engine):
    # Create database
    # Create Tables
    Pictures_model.Base.metadata.create_all(engine)
    Companies_model.Base.metadata.create_all(engine)
