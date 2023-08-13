#!/usr/bin/python3
"""file for testing the user class"""
import unittest
from models.user import User


class test_User(unittest.TestCase):
    """class for testing user class"""
    def test_user_attributes(self):
        """function for testing the attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
