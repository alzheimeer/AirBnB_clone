#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestAirBnBConsole(unittest.TestCase):
    """this will test the console"""

    def setUp(self):
        """Sets up test methods."""
        pass


if __name__ == "__main__":
    unittest.main()
