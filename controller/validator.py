import re
def name_validator(name):
    return bool(re.match("^[a-zA-Z\s]{3,30}$", name))
def username_validator(username):
    return bool(re.match("^[A-Za-z]{1}[A-Za-z0-9]{3,30}$",username))

def password_validator(password):
    return bool(re.match("^[A-Za-z0-9]{1}[A-Za-z0-9@]{7,30}$",password))