import unittest
from user import User 
class TestUser (unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.
    """
    def setUp (self):
        """
        First test to check if object is being initialized
        """
        self.new_user= User ("Instagram", "Duke", "12345")
    def test_save_user(self):
        """
        Test if the app is saving users into the list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1) 
if __name__ == '__main__':
    unittest.main()
