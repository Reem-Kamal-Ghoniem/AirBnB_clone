#!/usr/bin/python3
"""module containing unit tests for file storage class"""

import unittest

import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class FileStorageTest(unittest.TestCase):
    """tests for file storage class"""

    obj = BaseModel()

    def test_all(self):
        """tests all function in FileStorage"""
        FileStorageTest.obj.save()
        all_obj = storage.all()
        key = f"{type(FileStorageTest.obj).__name__}.{FileStorageTest.obj.id}"
        self.assertEqual(key in all_obj, True)

    def test_all_2(self):
        """tests all function in FileStorage"""
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_json_file_exists(self):
        """tests if save function creates json file"""
        FileStorageTest.obj.save()
        self.assertEqual(os.path.exists("file.json"), True)
