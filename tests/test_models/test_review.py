#!/usr/bin/python3
"""file for testtng using unittest style"""

import unittest
from models.review import Review


class test_Review(unittest.TestCase):
    """class for testing review class"""
    def test_review_attributes(self):
        """testing the attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
