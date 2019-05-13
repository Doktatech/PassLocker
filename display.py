import unittest
from user import User
def create_user (account,username,password,email):
    """
    Function for creating a new user object
    """
    new_user= User(account,username,password,email)
    return new_user
def save_user(user):
    """
    Function for saving user
    """
   user.save_user()
def find_user(account):
    """
    Function for finding user using username
    """
    return User.find_by_username(username)
def check_existing_user(account):
    """
    Function for checking if the user exists
    """
    return User.user_exists(account)
def display_users():    
    """
    Function for displaying users
    """

    return User.display_users() 