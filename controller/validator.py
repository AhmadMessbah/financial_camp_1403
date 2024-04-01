import re


def name_validator(name):
    return bool(re.match(r"^[A-Za-z]{3,15}[\s]?[A-Za-z]{3,15}$",name))


def username_validator(username):
    return bool(re.match("^[A-Za-z]{1}[A-Za-z0-9]{3,30}$", username))


def password_validator(password):
    return bool(re.match("^[A-Za-z0-9]{1}[A-Za-z0-9@]{7,30}$", password))


def amount_validator(amount):
    return bool(re.match("^[1-9]{1}[0-9]{2,30}$", amount))
# asdasds