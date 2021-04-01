#!/usr/bin/python3
"""
This module handles unittest for the class Amenity
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    Contains all the unitest associated with testing Amenity cls
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor setting up our object(s) for the tests
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Serves to the correct storage of the name
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
