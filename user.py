import pyperclip
class User :
    """
    Class that generates new instances of users.
    """
    user_list =[]
    def __init__ (self,account,username,password,email):
        self.account =account
        self.username=username
        self.password=password
        self.email=email
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
    def delete_user(self):
        """
        Delete method that allows us to delete users from the user_list
        """
        User.user_list.remove(self)
    @classmethod
    def find_by_username(cls,username):
        """
        Method for finding user by username        
        """
        for user in cls.user_list:
            if user.username ==username:
                return user
    @classmethod
    def user_exists(cls,account):
        """
        Method for checking user exists
        """
        for user in cls.user_list:
            if user.account == account:
                return True        
        return False
    @classmethod
    def display_users(cls):
        """
        Method for displays all users
        """
        return cls.user_list
    @classmethod
    def  copy_username(cls,username):
        user_found= User.find_by_username(username)
        pyperclip.copy(user_found.username)

    


    
    
