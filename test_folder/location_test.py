import unittest
from models.location import Location 


class TestLocation(unittest.TestCase):
    def setUp(self):
        self.name = "Glasgow"
        self.set = "River City"


    def test_location_has_name(self):
        self.assertEqual("Glasgow", self.name)
        
        
    def test_location_has_set(self):
        self.assertEqual("River City", self.set)

    