#!/usr/bin/python3
"""
    Module to create a unique FileStorage instance for an application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
