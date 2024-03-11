#!/usr/bin/python3
""" Defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Attributes of class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
