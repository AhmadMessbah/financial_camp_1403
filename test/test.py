#import controller.person_controller as p_control
from view.components import *

def login():
    if p_username.variable.get()==username.get() and p_password.variable.get()==password.get():
        return True

win = Tk()
win.geometry("300x200")
win.title("login")





# login
username = TextAndLabel(win, "Username", 20, 50)
password = TextAndLabel(win, "Password", 20, 90)

Button(win, text="Login", width=10, command=login).place(x=100, y=120)



win.mainloop()

def goto_person():
    pass
def goto_Trans():
    pass

#Homepage

win = Tk()
win.geometry("190x170")
win.title("Home Page")



Button(win, text="Person", width=10, command=goto_person).place(x=50, y=50)
Button(win, text="Transaction", width=10, command=goto_Trans).place(x=50, y=90)


win.mainloop()


def person_select():
    pass
def p_save_click():
    pass
def p_remove_click():
    pass
def p_edit_click():
    pass


#win_person
win = Tk()
win.geometry("570x500")
win.title("Persons")





# Person
Label(win, text="Person Info", font=("Arial", 16)).place(x=20, y=10)
p_id = TextAndLabel(win, "Id", 20, 50)
p_name = TextAndLabel(win, "Name", 20, 85)
p_family = TextAndLabel(win, "Family", 20, 120)
p_username= TextAndLabel(win, "Username", 300, 50)
p_password= TextAndLabel(win, "Password", 300, 85)

p_table = Table(win,
                None,
                ["id", "Name", "family", "Username", "Password"],
                [60, 110, 110, 110, 110],
                25,
                150,
                person_select)
Button(win, text="SavePerson", width=10, command=p_save_click).place(x=100, y=400)
Button(win, text="EditPerson", width=10, command=p_edit_click).place(x=190, y=400)
Button(win, text="RemovePerson", width=10, command=p_remove_click).place(x=280, y=400)


win.mainloop()

def trans_save_click():
    pass
def trans_edit_click():
    pass
def trans_remove_click():
    pass
def trans_select_all_click():
    pass
def trans_select_id_click():
    pass


#win_Trans
win = Tk()
win.geometry("450x550")
win.title("Transactions")





# Transaction
Label(win, text="Transaction Info", font=("Arial", 16)).place(x=20, y=10)
amount = TextAndLabel(win, "Amount", 20, 85)
Label(win, text="Type").place(x=20, y=120)
type = ttk.Combobox(win, values=['in','out'], state = 'readonly', width=17)
type.place(x=100, y = 120)
trans_table = Table(win,
                None,
                ["Person Id","Date and Time", "Amount", "Type"],
                [60, 100, 100, 100],
                20,
                190,
                person_select)
Button(win, text="Save Transaction", width=15, command=trans_save_click).place(x=30, y=430)
Button(win, text="Edit Transaction", width=15, command=trans_edit_click).place(x=150, y=430)
Button(win, text="Remove Transaction", width=15, command=trans_remove_click).place(x=270, y=430)
Button(win, text="select all Transaction", width=20, command=trans_select_all_click).place(x=50, y=470)
Button(win, text="select by id Transaction", width=20, command=trans_select_id_click).place(x=210, y=470)


win.mainloop()

