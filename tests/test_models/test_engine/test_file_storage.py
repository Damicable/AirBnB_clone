#!/usr/bin/python3
"""Unittest for FileStorage Class"""
import unittest
import json
from datetime import datetime
from time import sleep
from models.engine.file_storage import FileStorage

class test_FileStorage(unittest.TestCase):
    """This tests the FileStorage class"""

    def test_instances(self):
        """Tests FileStorage instantiation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """This tests the docstrings"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

if __name__ == '__main__':
    unittest.main()
