#!/usr/bin/python3
"""
This module check all things related to class Place
"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """
    Class that handles all tests for Place
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for our test objects
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Test the city id of an obj
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        Test user id's of our objs
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """
        Test the names attrs of an obj
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        Test the type of the description
        """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Tests the type of the attrs number_bathrooms
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """
        Test the attrs max_guest
        """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """
        Tests the attrs price_by_night
        """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """
        Test the latitutde attrs
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        Test longitude attrs of this
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """
        Test amenity attrs of the obj
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
