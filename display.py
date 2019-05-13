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
    