#!/usr/bin/python3
"""A unittest module for the City Class."""

import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage
from datetime import datetime
import time
from models.engine.file_storage import FileStorage
import json
import os
import re

class TestCity(unittest.TestCase):

    """Test cases for the City class"""

    def setup(self):
        """This sets up the test methods"""
        pass

    def tearaDown(self):
        """This resets the FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """This tests instantiation of City class"""

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """This tests the attributes of the class City."""
        attributes = storage.attributes()["City"]
        o = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()
