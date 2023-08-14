#!/usr/bin/python3
"""file for testing all console file"""
import unittest
from console import HBNBCommand


class test_console(unittest.TestCase):
    """class for testting console features"""
    def test_prompt(self):
        """testing the prompt"""
        self.assertEqual("(hbnb) ", self.console.prompt)

    def test_create(self):
        """testting create function"""
        self.console.onecmd("create BaseModel")

    def test_show(self):
        """testing show function"""
        self.console.onecmd("show BaseModel 1234-1234-1234")

    def test_destroy(self):
        """testting destroy function"""
        self.console.onecmd("destroy BaseModel 1234-1234-1234")

    def test_all(self):
        """testing all function"""
        self.console.onecmd("all BaseModel")

    def test_update(self):
        """testting update function"""
        self.console.onecmd("update BaseModel 1234-1234-1234 name 'New Name'")
