#import controller.person_controller as p_control
from tkinter import *
import tkinter.ttk as ttk



class Table:
    def refresh_table(self,data_list):
        for item in self.table.get_children():
            self.table.delete(item)

        if data_list:
            for data in data_list:
                self.table.insert("", END, values=data)

    def select(self, event):
        selected = self.table.item(self.table.focus())["values"]
        self.click(selected)

    def __init__(self, master, data_list, headings, widths, x, y, click):
        self.click = click
        columns = list(range(len(headings)))

        self.table = ttk.Treeview(master, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=headings[col])
            self.table.column(col, width=widths[col])

        if data_list:
            for data in data_list:
                self.table.insert("", END, values=data)

        self.table.bind("<ButtonRelease>", self.select)
        self.table.bind("<KeyRelease>", self.select)
        self.table.place(x=x, y=y)


class TextAndLabel:
    def __init__(self, master, text, x, y, distance=80):
        Label(master, text=text).place(x=x, y=y)
        self.variable = StringVar()
        Entry(master, textvariable=self.variable).place(x=x + distance, y=y)


class PersianCalendar:
    def change_date(self, event):
        self.day["values"] = list(
            range(1, JalaliDate.days_in_month(int(self.month.get()), int(self.year.get())) + 1, 1))
        self.persian_date = JalaliDate(int(self.year.get()), int(self.month.get()), int(self.day.get()))
        self.gregorian_date = self.persian_date.to_gregorian()

    def show_result(self):
        print("Result : ")

    def __init__(self, master, column_width, x, y):
        self.persian_date = JalaliDate.today()
        self.gregorian_date = JalaliDate.today().to_gregorian()

        # Year
        self.year = ttk.Combobox(master, width=column_width)
        self.year["values"] = list(range(1300, 1451, 1))
        self.year["state"] = "readonly"
        self.year.set(JalaliDate.today().year)
        self.year.bind("<<ComboboxSelected>>", self.change_date)
        self.year.place(x=x[0], y=y[0])

        # Month
        self.month = ttk.Combobox(master, width=column_width)
        self.month["values"] = list(range(1, 13, 1))
        self.month["state"] = "readonly"
        self.month.set(JalaliDate.today().month)
        self.month.bind("<<ComboboxSelected>>", self.change_date)
        self.month.place(x=x[1], y=y[1])

        # Day
        self.day = ttk.Combobox(master, width=column_width)
        self.day["state"] = "readonly"
        self.day["values"] = list(
            range(1, JalaliDate.days_in_month(JalaliDate.today().month, JalaliDate.today().year) + 1, 1))
        self.day.set(JalaliDate.today().day)
        self.day.bind("<<ComboboxSelected>>", self.change_date)
        self.day.place(x=x[2], y=y[2])


def login():
    pass

win = Tk()
win.geometry("300x200")
win.title("login")





# login
username = TextAndLabel(win, "Username", 20, 50)
password = TextAndLabel(win, "Password", 20, 90)

Button(win, text="Login", width=10, command=login).place(x=100, y=120)



win.mainloop()
if login():
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


def refresh_person_side():
    p_id.variable.set("")
    p_name.variable.set("")
    p_family.variable.set("")
    p_table.refresh_table(p_control.find_all()[1] if p_control.find_all()[0] else None)

def person_select(row):
    p_id.variable.set(row[0])
    p_name.variable.set(row[1])
    p_family.variable.set(row[2])
def person_select():
    pass
def p_save_click():
    status, message = p_control.save(
        p_name.variable.get(),
        p_family.variable.get())

    if status:
        msg.showinfo("Save", message)
        refresh_person_side()
    else:
        msg.showerror("Save Error", message)

def p_edit_click():
    status, message = p_control.edit(
        p_id.variable.get(),
        p_name.variable.get(),
        p_family.variable.get())

    if status:
        msg.showinfo("Edit", message)
        refresh_person_side()
    else:
        msg.showerror("Edit Error", message)

def p_remove_click():
    status, message = p_control.remove(p_id.variable.get())

    if status:
        msg.showinfo("Remove", message)
        refresh_person_side()
    else:
        msg.showerror("Remove Error", message)





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

