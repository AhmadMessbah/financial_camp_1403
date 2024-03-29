#import controller.person_controller as p_control
from view.components import *

def login(username , password):
    pass


login_win = Window('Login', 400, 300)
# person_win = Window('Persons', 400, 300)
# Tr_win = Window('Transations', 400, 300)
# Home_win = Window('Home', 400, 300)




# login
username = TextAndLabel(login_win, "Username", 20, 50)
password = TextAndLabel(login_win, "Password", 20, 90)

Button(login_win, text="Login", width=10, command=login()).place(x=20, y=400)




# print(p_control.save("mohsen", "akbari"))
# print(p_control.edit(3,"mohsen", "mohseni"))
# print(p_control.remove(3))
# print(p_control.find_all())
# print(p_control.find_by_id(1))


# this is test by rasta banaii

