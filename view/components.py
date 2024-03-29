from tkinter import *
import tkinter.ttk as ttk
from persiantools.jdatetime import JalaliDate


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
