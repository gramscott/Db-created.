import unittest
from models.user import User 

class TestUser(unittest.TestCase):


    def setUp(self):
        self.user1 = User("Susan", "TV Producer", id = None)
        self.user2 = User("Greg", "Assistant Director")

    def test_user1_has_name(self):
        self.assertEqual("Susan", self.user1.name)

    def test_user1_has_job(self):
        self.assertEqual("TV Producer", self.user1.job)

    def test_user1_has_id(self):
        self.assertEqual(None, self.user1.id)

    def test_user2_has_name(self):
        self.assertEqual("Greg", self.user2.name)

    def test_user2_has_job(self):
        self.assertEqual("Assistant Director", self.user2.job)

    def test_user2_has_id(self):
        self.assertEqual(None, self.user2.id)
