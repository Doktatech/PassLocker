#!/usr/bin/env python3.6
import pyperclip
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
def main():
    print("\033[1;35;40m PASSWORD-LOCKER APP\n")
    print("")
    prom = input("Hello, Welcome to Password-Locker there whats your name?: ")
    print("  ")
    print("Kaaribu, " + prom + ", To get you started up kindly choose one of the following")
    print(" ")    
    while True:
        print("Use these any of these short codes : \n ca - create an account\n da - display username\n fu - find a user\n ex - exit the user list ")
        print(" ")
        short_code = input('Enter : ').lower().strip()
        if short_code == 'ca':
            print('To create a new account: ')
            first_name = input("Please enter the first name: ")
            last_name = input("Please enter your last name: ")
            password = input("Please enter your password: ")
            email = input("Please enter your emailId: ")
            print("\033[1;32;1m  \n")
            print("Bravoo!" + first_name +" "+ last_name + " You have successfully registered at PasswordLocker using password " + password)
            print("------------------------------------------------------------------passlocker ")
            print("To save an account, Enter the respective credentials :  ")
            print("------------------------------------------------------------------passlocker")
            account = input("Enter the name of the account that you want to store:  ")
            username = input("Enter the username you are using:  ")
            password = input("Enter your password:  ")
            email =input ("Enter the email address for stated account:  ")
            save_user(User(account, username, password,email))
            print("\033[1;35;1m You have successfully saved your Credentials \n")            
            print("\033[1;35;1m  \n")
        elif short_code == "da":
            if display_users():
                print("Here is a list of all your Accounts")
                print("\n")               
                user = User.display_user()
                print("\033[1;37;1m  \n")
                print(f"Site: {user.account} \n User Name: {user.username} \n Password: {user.password}")
                  
            else:
                print("\033[1;35;1m  \n")
                print(" ")
                print("You don't seem to have any accounts created yet")       
if __name__ == '__main__':
	main()