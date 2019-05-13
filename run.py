#!/usr/bin/env python3.6
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
def del_user(user):
    """
    Function that removes a user from the list
    """
    user.delete_user()
def find_user(username):
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