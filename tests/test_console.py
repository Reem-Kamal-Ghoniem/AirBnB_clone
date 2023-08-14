#!/usr/bin/python3
"""file for testing all console file"""
import unittest
from console import HBNBCommand


class test_console(unittest.TestCase):
    """class for testting console features"""
    def test_prompt(self):
        """testing the prompt"""
        self.assertEqual("(hbnb) ", self.console.prompt)
