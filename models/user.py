#!/usr/bin/python3
"""class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a User"""
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
