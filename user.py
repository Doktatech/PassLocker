class User :
    """
    Class that generates new instances of users.
    """
    user_list =[]
    def __init__ (self,account,username,password):
        self.account =account
        self.username=username
        self.password=password
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
    def delete_user(self):
        """
        Delete method that allows us to delete users from thhe user_list
        """
        User.user_list.remove(self)
    
