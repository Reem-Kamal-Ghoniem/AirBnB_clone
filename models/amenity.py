#!/usr/bin/python3
"""a file that contains ameity class
that inherits from BAseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing an Amenity
    and inheriting from BaseModel"""
    name = ""
