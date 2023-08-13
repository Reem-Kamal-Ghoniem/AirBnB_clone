#!/usr/bin/python3
"""testing file with unittest style"""
import unittest
from models.city import City


class test_City(unittest.TestCase):
    """class for testing class city"""
    def test_city_attributes(self):
        """testting attributes values"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
