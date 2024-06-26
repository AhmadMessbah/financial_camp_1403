#import controller.person_controller as p_control
from tkinter import *
import tkinter.ttk as ttk
from view.components import *


class Pages:

    # Pages Management

    def close_win(self):
        win.destroy()

    def show_homepage(self):
        # Homepage Page Design
        win = Tk()
        win.geometry("190x170")
        win.title("Home Page")
        # bg_hp=PhotoImage(file="financial.jpg")
        Label(win, text="Home Page", font=("Helvetica", 16)).place(x=20, y=10)
        Button(win, text="Person", width=10, command= self.goto_person).place(x=50, y=50)
        Button(win, text="Transaction", width=10, command= self.goto_Trans).place(x=50, y=90)
        win.mainloop()

    def login(self):
        if self.username.variable.get()=="admin" and self.password.variable.get() =="admin":
            self.show_homepage()

    def show_person_page(self):
    # Person Page Design

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
                        None,
                        ["id", "Name", "family", "Username", "Password"],
                        [60, 110, 110, 110, 110],
                        25,
                        150,
                        person_select)
        Button(win, text="Save Person", width=12, command=self.p_save_click).place(x=130, y=400)
        Button(win, text="Edit Person", width=12, command=self.p_edit_click).place(x=230, y=400)
        Button(win, text="Remove Person", width=12, command=self.p_remove_click).place(x=330, y=400)
        Button(win, text="Home Page", width=12, command=self.show_homepage).place(x=230, y=460)
        win.mainloop()

    def show_trans_page(self):
        # Transaction Page Design
        win = Tk()
        win.geometry("410x570")
        win.title("Transactions")
        # bg_tran = PhotoImage(file = "trans.jpg")
        Label(win, text="Transaction Info", font=("Helvetica", 16)).place(x=20, y=10)
        amount = TextAndLabel(win, "Amount", 20, 85)
        Label(win, text="Type").place(x=20, y=120)
        type = ttk.Combobox(win, values=['in', 'out'], state='readonly', width=17)
        type.place(x=100, y=120)
        trans_table = Table(win,
                            None,
                            ["Person Id", "Date and Time", "Amount", "Type"],
                            [60, 100, 100, 100],
                            20,
                            190,
                            self.person_select)
        Button(win, text="Save Transaction", width=15, command=self.trans_save_click).place(x=30, y=430)
        Button(win, text="Edit Transaction", width=15, command=self.trans_edit_click).place(x=150, y=430)
        Button(win, text="Remove Transaction", width=15, command=trans_remove_click).place(x=270, y=430)
        Button(win, text="select all Transaction", width=20, command=trans_select_all_click).place(x=50, y=470)
        Button(win, text="select by id Transaction", width=20, command=trans_select_id_click).place(x=210, y=470)
        Button(win, text="Home Page", width=12, command=self.goto_homepage).place(x=150, y=530)
        win.mainloop()









# Person Functions
def refresh_person_side():
    Pages.self.p_id.variable.set("")
    Pages.self.p_name.variable.set("")
    Pages.self.p_family.variable.set("")
    Pages.self.p_username.variable.set("")
    Pages.self.p_password.variable.set("")
    Pages.self.p_table.refresh_table(p_control.find_all()[1] if p_control.find_all()[0] else None)

def person_select(row):
    Pages.self.p_id.variable.set(row[0])
    Pages.self.p_name.variable.set(row[1])
    Pages.self.p_family.variable.set(row[2])
    Pages.self.p_username.variable.set(row[3])
    Pages.self.p_password.variable.set(row[4])
def p_save_click():
    status, message = p_control.save(
        Pages.self.p_name.variable.get(),
        Pages.self.p_family.variable.get(),
        Pages.self.p_username.variable.get(),
        Pages.self.p_password.variable.get())

    if status:
        msg.showinfo("Save", message)
        refresh_person_side()
    else:
        msg.showerror("Save Error", message)

def p_edit_click():
    status, message = p_control.edit(
        Pages.self.p_id.variable.get(),
        Pages.self.p_name.variable.get(),
        Pages.self.p_family.variable.get(),
        Pages.self.p_username.variable.get(),
        Pages.self.p_password.variable.get())

    if status:
        msg.showinfo("Edit", message)
        refresh_person_side()
    else:
        msg.showerror("Edit Error", message)

def p_remove_click():
    status, message = p_control.remove(Pages.self.p_id.variable.get())

    if status:
        msg.showinfo("Remove", message)
        refresh_person_side()
    else:
        msg.showerror("Remove Error", message)


# Transaction Functions
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







# login Page Design
win = Tk()
win.geometry("300x200")
win.title("login")
#bg_login=PhotoImage(file="financial.jpg")
Label(win, text="Login Page", font=("Helvetica", 16)).place(x=20, y=10)
username = TextAndLabel(win, "Username", 20, 50)
password = TextAndLabel(win, "Password", 20, 90)
Button(win, text="Login", width=10, command=Pages.login).place(x=100, y=120)
win.mainloop()










