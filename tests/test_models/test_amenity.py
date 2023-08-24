#!/usr/bin/python3
"""A unittest module for the Amenity class"""

from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from model.engine.file_storage import FileStorage
import unittest
from datetime import datetime
import time
import json
import os
import re


class TestAmenity(unittest.TestCase):
    """This tests cases for the Amenity class"""

    def setup(self):
        """This sets up the test methods"""
        pass

    def tearDown(self):
        """This tears down the test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """This resets the FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """This tests the instantiation of the Amenity class."""

        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """This tests the attributes of the Amenity class."""
        attributes = storage.attributes()["Amenity"]
        o = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
