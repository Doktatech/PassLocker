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
    def tearDown(self):
        """
        This method cleans up everything after each test
        """
        User.user_list= []
    def test_save_user(self):
        """
        Test if the app is saving users into the list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1) 
    def test_save_multiple_user(self):
        """
        A test method that checks if we can save multiple users
        """
        self.new_user.save_user()        
        test_user = User("Instagram", "Duke", "12345")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
if __name__ == '__main__':
    unittest.main()
