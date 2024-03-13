import json


class User:
    def __init__(self, username, password, is_admin):
        self.username = username
        self.password = password
        self.is_active = True
        self.is_admin = is_admin

    def deactivate(self):
        self.is_active = False

    def promote(self):
        self.is_admin = True 

    def toString(self):
        return "{" + self.username + ":" + self.password + ":" + str(self.is_admin) + "}"

