#!/usr/bin/python3
"""file that test the BaseModel class using UnitTest"""

from datetime import datetime
from models.base_model import BaseModel
import unittest


class BaseModel_test(unittest.TestCase):
    """class for teseting BaseModel class"""
    def setUp(self):
        """Initializes for the tests."""
        self.test = BaseModel()
        self.dict = self.test.to_dict()

    def test_instance_creation(self):
        """Testting if BaseModel is created correctly."""
        self.assertIsInstance(self.test, BaseModel)
        self.assertIsInstance(self.test.created_at, datetime)
        self.assertIsInstance(self.test.updated_at, datetime)

    def test_str(self):
        """Testting __str__ method"""
        out_str = "[BaseModel] ({}) {}".\
            format(self.test.id, self.test.__dict__)
        self.assertEqual(str(self.test), out_str)

    def test_save(self):
        """Testting save method"""
        old_updated_at = self.test.updated_at
        self.test.save()
        self.assertNotEqual(old_updated_at, self.test.updated_at)

    def test_to_dict(self):
        """Testting to_dict method"""
        out_dict = {
            '__class__': 'BaseModel',
            'id': self.test.id,
            'created_at': self.test.created_at.isoformat(),
            'updated_at': self.test.updated_at.isoformat()
        }
        self.assertEqual(self.dict, out_dict)

    def test_from_dict_with_created_at_string(self):
        """Test BaseModel recreation with created_at"""
        dict_with_string = self.dict.copy()
        dict_with_string['created_at'] = "2023-08-10T12:34:56.251234"
        mod = BaseModel(**dict_with_string)
        self.assertEqual(mod.created_at.isoformat(), "2023-08-10T12:34:56.251234")

    def test_from_dict_with_updated_at_string(self):
        """Test BaseModel recreation with updated_at as string."""
        model_dict_with_string = self.dict.copy()
        model_dict_with_string['updated_at'] = "2023-08-10T12:34:56.251234"
        mod = BaseModel(**model_dict_with_string)
        self.assertEqual(mod.updated_at.isoformat(), "2023-08-10T12:34:56.251234")

    def test_from_dict_with_class_key(self):
        """Test recreation with a __class__ key."""
        model_dict_with_class_key = self.dict.copy()
        model_dict_with_class_key['__class__'] = 'NotBaseModel'
        out_model = BaseModel(**model_dict_with_class_key)
        self.assertEqual(out_model.__class__.__name__, 'BaseModel')
