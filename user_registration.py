import hashlib
import os
from flask_login import UserMixin
from random import randrange

class User(UserMixin):
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

def user_registration(user):
    username = user.username
    password = user.password
    users_dict = get_users_dict()
    key = hashlib.sha256(password.encode("utf-8")).hexdigest()
    if username not in users_dict:
        with open("users.txt", "a") as users:
                users.write(f"{username}:{key}\n")
                users_dict[username] = key
                return users_dict, "Registration is successful"
    else:
        return users_dict, "This username already exist"

def user_login(user):
    username = user.username
    password = user.password
    users_dict = get_users_dict()
    if username in users_dict:
        key = users_dict[username]
        new_key = hashlib.sha256(password.encode("utf-8")).hexdigest()
        if new_key == key:
            return users_dict, "login succesfully"
        else: 
            return users_dict, "uncorrect login or password"
    else:
        return users_dict, "uncorrect login or password"
    

def get_users_dict():
    users_dict = dict()
    with open("users.txt") as users:
        for line in users:
            line = line.strip()
            if line != "":
                user = line.split(":")[0]
                key = line.split(":")[1]
                users_dict[user] = key
    return users_dict