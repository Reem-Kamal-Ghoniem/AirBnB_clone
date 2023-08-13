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
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    if key == 'created_at':
                        self.created_at = \
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        self.updated_at = \
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
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
        out = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                out[key] = value.isoformat()
            else:
                out[key] = value
        out["__class__"] = self.__class__.__name__
        return out
