#!/usr/bin/python3
"""
a file that contains clas City"""

from models.base_model import BaseModel

class City(BaseModel):
    """Class representing a City
    that will inherits from BaseModel"""
    state_id = ""
    name = ""
