#!/usr/bin/python3
"""
file includes the BaseModel class
"""

import uuid
from datetime import datetime


class BaseModel:
    """class for defining all common
    attributes and methods for other classes"""
    def __init__(self, *args, **kwargs):
        """initiallization of BaseModel"""
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    if key == 'created_at':
                        self.created_at = \
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        self.updated_at = \
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)

                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """returns string representation"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary"""
        out_dict = self.__dict__.copy()
        out_dict['__class__'] = type(self).__name__
        out_dict['created_at'] = self.created_at.isoformat()
        out_dict['updated_at'] = self.updated_at.isoformat()
        return out_dict
