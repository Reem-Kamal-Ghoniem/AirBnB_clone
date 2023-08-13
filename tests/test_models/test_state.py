#!/usr/bin/python3
"""a unittest file for testing State class"""
import unittest
from models.state import State


class test_State(unittest.TestCase):
    """slass test_state for testing state class"""
    def test_state_attributes(self):
        """testing values"""
        state = State()
        self.assertEqual(state.name, "")
