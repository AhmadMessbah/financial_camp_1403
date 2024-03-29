from tkinter import Tk, Button
import tkinter.messagebox as msg
from components import *
import project.controller.person_controller as p_control

def refresh_person_side():
    p_id.variable.set("")
    p_name.variable.set("")
    p_family.variable.set("")
    p_table.refresh_table(p_control.find_all()[1] if p_control.find_all()[0] else None)

def person_select(row):
    p_id.variable.set(row[0])
    p_name.variable.set(row[1])
    p_family.variable.set(row[2])


def book_select(row):
    pass


def p_save_click():
    status, message= p_control.save(
        p_name.variable.get(),
        p_family.variable.get())

    if status:
        msg.showinfo("Save" , message)
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


def b_save_click():
    pass


def b_edit_click():
    pass


def b_remove_click():
    pass


def borrow_click():
    pass


win = Tk()
win.title("Library")
win.geometry("800x600")

# Person
Label(win, text="Person Info", font=("Arial", 16)).place(x=20, y=10)
p_id = TextAndLabel(win, "Id", 20, 50)
p_name = TextAndLabel(win, "Name", 20, 85)
p_family = TextAndLabel(win, "Family", 20, 120)

p_table = Table(win,
                None,
                ["id", "Name", "family"],
                [60, 100, 100],
                20,
                150,
                person_select)
Button(win, text="SavePerson", width=10, command=p_save_click).place(x=20, y=400)
Button(win, text="EditPerson", width=10, command=p_edit_click).place(x=110, y=400)
Button(win, text="RemovePerson", width=10, command=p_remove_click).place(x=200, y=400)

# Book
Label(win, text="Book Info", font=("Arial", 16)).place(x=500, y=10)
b_id = TextAndLabel(win, "Id", 500, 50)
b_name = TextAndLabel(win, "Name", 500, 85)
b_writer = TextAndLabel(win, "Writer", 500, 120)

b_table = Table(win,
                None,
                ["id", "Name", "Writer"],
                [60, 100, 100],
                500,
                150,
                book_select)

Button(win, text="SaveBook", width=10, command=b_save_click).place(x=500, y=400)
Button(win, text="EditBook", width=10, command=b_edit_click).place(x=590, y=400)
Button(win, text="RemoveBook", width=10, command=b_remove_click).place(x=680, y=400)

Button(win,
       text="Borrow",
       width=10,
       height=2,
       bg="lightgreen",
       font=("Arial", 16),
       command=borrow_click).place(x=330, y=450)


refresh_person_side()

win.mainloop()
