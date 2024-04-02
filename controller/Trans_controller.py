from controller.validator import amount_validator
from model.da.trans_da import TransDa

def tr_save(id, date_time, amount, type):
    try:
        if amount_validator(amount):
            da = TransDa()
            da.save(id, date_time, amount, type)
            return True, "Saved"
        else:
            return False, "Error : Invalid Data"
    except Exception as e:
        return False, f"Error : {e}"

def tr_find_all():
    try:
        da = TransDa()
        return True, da.find_all()
    except Exception as e:
        return False, f"Error : {e}"

def tr_find_by_id(id):
    try:
        da = TransDa()
        return True, da.find_by_id(id)
    except Exception as e:
        return False, f"Error : {e}"

def tr_balance(id):
    balance = 0
    try:
        da = TransDa()
        trs = da.find_by_id(id)
        for item in trs:
            if da.type == 0:
                balance -= da.amount
            else:
                balance += da.amount
        return balance
    except Exception as e:
        return False, f"Error : {e}"