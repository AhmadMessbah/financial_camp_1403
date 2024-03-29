import re


def name_validator(name):
    return bool(re.match("^[a-zA-Z\s]{3,30}$", name))
