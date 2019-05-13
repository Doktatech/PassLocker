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
def main():
    print("\033[1;35;40m PASSWORD-LOCKER APP\n")
    print("")
    prom = input("Hello, Welcome to Password-Locker there whats your name?: ")
    print("  ")
    print("Kaaribu, " + prom + ", To get you started up kindly choose one of the following")
    print(" ")    
    while True:
        print("Use any of these short codes : \n ca - create an account\n da - display username\n fu - find a user\n ex - exit the user list ")
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
                print("Here is a list of saved Accounts")
                print("\n") 
                for user in display_users():              
               #  user = User.display_user()
               #  print("\033[1;37;1m  \n")
                  print(f"Site: {user.account} \n User Name: {user.username} \n Password: {user.password}")
                  
            else:
                print("\033[1;35;1m  \n")
                print(" ")
                print("You don't seem to have any accounts created yet")  
        elif short_code == "fu":
            print("Enter the username you want to search for")
            search_username= input()
            if find_user(search_username):
               search_user = find_user(search_username)
               print(f"{search_user.username} ")
               print('-' * 30)
               print(f"Username.......{search_user.username}")
               print(f"Email address.......{search_user.email}")
            else:
               print("That contact does not exist")
        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
	main()