#!/usr/bin/python3
"""
module containing file storage engine
for storing objects in a file with json format
"""


import json


class FileStorage:
    """class FileStorage
    that serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf=8") as f:
            objects_dict = {}

            for key, value in FileStorage.__objects.items():
                objects_dict[key] = value.to_dict()

            json.dump(objects_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        from models.base_model import BaseModel

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                for key, value in json.load(f).items():
                    self.new(BaseModel(**value))
        except Exception:
            pass
