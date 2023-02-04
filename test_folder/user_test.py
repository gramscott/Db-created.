







import unittest
from models.user import User 



class TestUser(unittest.TestCase):

    def setUp(self):
        self.name = "Susan"
        self.job = "Tv Producer"


    def test_user_has_name(self):
        self.assertEqual("Susan", self.name)

    def test_user_has_job(self):
        self.assertEqual("Tv Producer", self.job)





