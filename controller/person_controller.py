import re

from controller.validator import name_validator
from model.da.person_da import PersonDa


def pr_save(name,family):
    try:
        if name_validator(name) and name_validator(family):
            da = PersonDa()
            da.save(name,family)
            return True, "Saved"
        else:
            return False, "Error : Invalid Data"
    except Exception as e:
        return False, f"Error : {e}"


def pr_edit(id, name,family):
    try:
        if name_validator(name) and name_validator(family):
            da = PersonDa()
            da.edit(id, name,family)
            return True, "Edited"
        else:
            return False, "Error : Invalid Data"
    except Exception as e:
        return False, f"Error : {e}"

def pr_remove(id):
    try:
        da = PersonDa()
        da.remove(id)
        return True, "Removed"
    except Exception as e:
        return False, f"Error : {e}"

def pr_find_all():
    try:
        da = PersonDa()
        return True, da.find_all()
    except Exception as e:
        return False, f"Error : {e}"

def pr_find_by_id(id):
    try:
        da = PersonDa()
        return True, da.find_by_id(id)
    except Exception as e:
        return False, f"Error : {e}"