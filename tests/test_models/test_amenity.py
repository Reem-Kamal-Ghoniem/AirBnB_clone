#!/usr/bin/python3
"""testting class amenity using unittest style"""

import unittest
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """class for testing amenity class"""
    def test_amenity_attributes(self):
        """testing values"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
