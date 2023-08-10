#!/usr/bin/python3
"""This module contains the User class implementation"""
from models.base_model import BaseModel


class User(BaseModel):
    """A user class that contains user attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
