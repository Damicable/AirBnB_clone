#!/usr/bin/python3
"""This module contains the Review class implementation"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A review class that contains state attributes"""
    place_id = ""
    user_id = ""
    text = ""
