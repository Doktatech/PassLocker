import unittest
import pyperclip
from user import User 
class TestUser (unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.
    """
    def setUp (self):
        """
        First test to check if object is being initialized
        """
        self.new_user= User ("NetFlix", "Duke", "12345","Netflix@user.com")
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
        test_user = User("NetFlix", "Duke", "12345","Netflix@user.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    def test_delete_user(self):
        """
        A test method for checking if we can remove a user from our list
        """
        self.new_user.save_user()
        test_user =User("NetFlix", "Duke","12345","Netflix@user.com")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
    def test_find_user_by_username(self):
        """
        A test to confirm if we can find a user using their username
        """
        self.new_user.save_user()
        test_user = User("NetFlix", "Duke", "12345","Netflix@user.com")
        test_user.save_user()
        found_user = User.find_by_username("Duke")
        #self.assertEqual(found_user.email, test_user.email)
    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("NetFlix", "Duke", "12345","Netflix@user.com")
        test_user.save_user()
        user_exists=User.user_exists ("NetFlix")
        self.assertTrue(user_exists)
    def test_display_users (self):
        """
        Test method that returns all users in the list
        """
        self.assertEqual(User.display_users(),User.user_list)
    def test_copy_username(self):
        """
        Test to confirm that username is being copied from the contact found
        """
        self.new_user.save_user()
        User.copy_username("Duke")    
        self.assertEqual(self.new_user.username,pyperclip.paste())
if __name__ == '__main__':
    unittest.main()
