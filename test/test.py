from tkinter import *
import tkinter.ttk as ttk
from view.components import *
import controller.person_controller as p_control
import controller.Trans_controller as t_control

# Pages Management

def close_win():
    win.withdraw()

def goto_homepage():
    close_win()
    # Homepage Page Design
    win = Tk()
    win.geometry("190x170")
    win.title("Home Page")
    # bg_hp=PhotoImage(file="financial.jpg")
    Label(win, text="Home Page", font=("Helvetica", 16)).place(x=20, y=10)
    Button(win, text="Person", width=10, command= goto_person).place(x=50, y=50)
    Button(win, text="Transaction", width=10, command= goto_trans).place(x=50, y=90)
    win.mainloop()


def goto_person():
# Person Page Design
    close_win()
    win = Tk()
    win.geometry("560x500")
    win.title("person")
    # bg_pers = PhotoImage(file = "pers.jpeg")
    Label(win, text="Person Information", font=("Helvetica", 16)).place(x=20, y=10)
    p_id = TextAndLabel(win, "Id", 20, 50)
    p_name = TextAndLabel(win, "Name", 20, 85)
    p_family = TextAndLabel(win, "Family", 20, 120)
    p_username = TextAndLabel(win, "Username", 300, 50)
    p_password = TextAndLabel(win, "Password", 300, 85)

    p_table = Table(win,
                    p_control.find_all()[1],
                    ["Id", "Name", "Family", "Username", "Password"],
                    [60, 110, 110, 110, 110],
                    25,
                    150,
                    person_select)
    Button(win, text="Save Person", width=12, command=p_save_click).place(x=130, y=400)
    Button(win, text="Edit Person", width=12, command=p_edit_click).place(x=230, y=400)
    Button(win, text="Remove Person", width=12, command=p_remove_click).place(x=330, y=400)
    win.mainloop()

def goto_trans():
    close_win()
     # Transaction Page Design
    win = Tk()
    win.geometry("410x570")
    win.title("Transactions")
    # bg_tran = PhotoImage(file = "trans.jpg")
    Label(win, text="Transaction Info", font=("Helvetica", 16)).place(x=20, y=10)
    p_id = TextAndLabel(win, "Person ID", 21, 70)
    t_amount = TextAndLabel(win, "Amount", 20, 105)
    Label(win, text="Type").place(x=20, y=140)
    t_type = ttk.Combobox(win, values=['in', 'out'], state='readonly', width=17)
    t_type.place(x=100, y=140)
    trans_table = Table(win,
                        t_control.find_all()[1],
                        ["Person Id", "Date and Time", "Amount", "Type"],
                        [60, 100, 100, 100],
                        20,
                        190,
                        trans_select)
    Button(win, text="Save Transaction", width=43, command=trans_save_click).place(x=50, y=430)
    Button(win, text="find all Transaction", width=20, command=trans_find_all_click).place(x=50, y=470)
    Button(win, text="find by id Transaction", width=20, command=trans_find_id_click).place(x=210, y=470)
    win.mainloop()



    #Todo: we need to get the p_username and p_pasword from goto_person but our function can not have any input so it can be used in command
def login():
    #if username.variable.get()==p_username.variable.get() and password.variable.get()==p_password.variable.get():
     #For testing we can use the code below
    if username.variable.get()=="admin" and password.variable.get() =="admin":
        goto_homepage()


# Person Functions
def refresh_person_side():
    p_id.variable.set("")
    p_name.variable.set("")
    p_family.variable.set("")
    p_username.variable.set("")
    p_password.variable.set("")
    p_table.refresh_table(p_control.find_all()[1] if p_control.find_all()[0] else None)

def person_select(row):
    p_id.variable.set(row[0])
    p_name.variable.set(row[1])
    p_family.variable.set(row[2])
    p_username.variable.set(row[3])
    p_password.variable.set(row[4])

def p_save_click():
    status, message = p_control.pr_save(
        p_name.variable.get(),
        p_family.variable.get(),
        p_username.variable.get(),
        p_password.variable.get())

    if status:
        msg.showinfo("Save", message)
        refresh_person_side()
    else:
        msg.showerror("Save Error", message)

def p_edit_click():
    status, message = p_control.pr_edit(
        p_id.variable.get(),
        p_name.variable.get(),
        p_family.variable.get(),
        p_username.variable.get(),
        p_password.variable.get())

    if status:
        msg.showinfo("Edit", message)
        refresh_person_side()
    else:
        msg.showerror("Edit Error", message)

def p_remove_click():
    status, message = p_control.pr_remove(p_id.variable.get())

    if status:
        msg.showinfo("Remove", message)
        refresh_person_side()
    else:
        msg.showerror("Remove Error", message)

def trans_select(row):
    p_id.variable.set(row[0])
    t_amount.variable.set(row[2])
    t_type.variable.set(row[3])
    

def refresh_trans_side():
    p_id.variable.set("")
    t_amount.variable.set("")
    t_type.variable.set("")
    trans_table.refresh_table(t_control.find_all()[1] if t_control.find_all()[0] else None)


# Transaction Functions
def trans_save_click():
    status, message = t_control.tr_save(
        p_id.variable.get(),
        Jalalidate.today(),
        t_amount.variable.get(),
        t_type.get())

    if status:
        msg.showinfo("Save", message)
        refresh_trans_side()
    else:
        msg.showerror("Save Error", message)



def trans_find_all_click():
    status, message = t_control.tr_find_all()

    if status:
        msg.showinfo("found", message)
        refresh_trans_side()
    else:
        msg.showerror("finding Error", message)


def trans_find_id_click():
    status, message = t_control.tr_save(p_id.variable.get())

    if status:
        msg.showinfo("found", message)
        refresh_trans_side()
    else:
        msg.showerror("finding Error", message)    



# login Page Design
win = Tk()
win.geometry("300x200")
win.title("login")
#bg_login=PhotoImage(file="financial.jpg")
Label(win, text="Login Page", font=("Helvetica", 16)).place(x=20, y=10)
username = TextAndLabel(win, "Username", 20, 50)
password = TextAndLabel(win, "Password", 20, 90)
Button(win, text="Login", width=10, command=login).place(x=100, y=120)
win.mainloop()

