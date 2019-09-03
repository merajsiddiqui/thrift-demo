'''
Importing data types defined in demo.thrift
User
InvalidUser
'''
from gen_py.UserService.ttypes import User, InvalidUser
import json
'''
@class : Any choice of your name for example UserService
Write the class as you write without thrift just one thing  it will contain the method exposed in demo.thrift
@method: getUser
'''

class UserService(object):

    users = []
    
    def __init__(self):
        user_json_file = "users.json"
        user_file = open(user_json_file, "r")
        users_json_data = user_file.read()
        user_data = json.loads(users_json_data)
        user_file.close()
        self.users = user_data

    def getUser(self, userId):
        foundUser = None
        for user in self.users:
            if user["id"] == userId:
                foundUser = user
                break
        if foundUser is None:
            raise InvalidUser(message="User Id does not exist")
        else:
            user_details = User(foundUser["name"], foundUser["id"], foundUser["active"])
            return user_details
        

