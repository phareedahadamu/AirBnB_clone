#!/usr/bin/python3
""" Describes a class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Attributes of class Review"""
    place_id = ""
    user_id = ""
    text = ""
