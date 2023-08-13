#!/usr/bin/python3
"""a python file that contais class review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a Review that
    inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
