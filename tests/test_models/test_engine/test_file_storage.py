#!/usr/bin/python3
"""module containing unit tests for file storage class"""

import unittest

import os

from click import File
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class FileStorageTest(unittest.TestCase):
    """tests for file storage class"""

    obj = BaseModel()

    def test_attributes(self):
        """tests if attributes exist for FileStorage Class"""
        self.assertEqual(hasattr(FileStorage, "_FileStorage__file_path"), True)
        self.assertEqual(hasattr(FileStorage, "_FileStorage__objects"), True)

    def test_all(self):
        """tests all function in FileStorage"""
        FileStorageTest.obj.save()
        all_obj = storage.all()
        key = f"{type(FileStorageTest.obj).__name__}.{FileStorageTest.obj.id}"
        self.assertEqual(key in all_obj, True)

    def test_all_2(self):
        """tests all function in FileStorage"""
        objects = storage._FileStorage__objects  # type: ignore
        self.assertEqual(storage.all(), objects)

    def test_json_file_exists(self):
        """tests if save function creates json file"""
        FileStorageTest.obj.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_new(self):
        """tests new function"""
        new_model = BaseModel()
        key = f"{type(new_model).__name__}.{new_model.id}"
        objs = storage.all()
        self.assertEqual(key in objs, True)

    def test_reload(self):
        """test reload function"""
        FileStorageTest.obj.save()
        self.assertEqual(os.path.exists("file.json"), True)
        objs = storage.all()
        FileStorage._FileStorage__objects = {}  # type: ignore
        self.assertEqual(objs == FileStorage._FileStorage__objects, False)
        storage.reload()
        key = f"{type(FileStorageTest.obj).__name__}.{FileStorageTest.obj.id}"
        self.assertEqual(key in FileStorage._FileStorage__objects, True)
