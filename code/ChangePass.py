import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import mysql.connector

# Todo: connect your database
DB_project = mysql.connector.connect(
  host="",
  user="",
  password="",
  port=3306,
  database = ""
)
my_cursor = DB_project.cursor(dictionary=True)
DB_project.autocommit = True

class ChanePassword(ttk.Frame):
    def __init__(self, master,username):
        super().__init__(master, padding=(10, 5))
        self.pack(fill=BOTH, expand=YES)
        self.username = username
        # form variables
        # self.username = ttk.StringVar(value="")
        self.pre_pass = ttk.StringVar(value="")
        self.new_pass = ttk.StringVar(value="")

        # form entries
        # self.create_form_entry("User ID", self.username)
        self.create_form_entry("Previous Password", self.pre_pass)
        self.create_form_entry("New Password", self.new_pass)
        self.create_buttonbox()

    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=10, ipadx=20, fill=X, expand=YES)

        ent = ttk.Entry(master=container, textvariable=variable,show="*")
        ent.pack(side=LEFT, padx=5)

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

    def on_submit(self):
        """Print the contents to console and return the values."""
        # print("Name:", self.username.get())
        # print("Address:", self.pre_pass.get())
        # print("Phone:", self.new_pass.get())
        # return self.username.get(), self.pre_pass.get(), self.new_pass.get()

        # uid = self.username.get()
        ppass = self.pre_pass.get()
        npass = self.new_pass.get()
        
        
        
        my_cursor.execute(f"SELECT UID from bank_user where username=\"{self.username}\";")
        uid = list(my_cursor)[0]['UID']
        
        
        args = (uid,ppass,npass,)
        my_cursor.callproc("change_password",args)
        tmp = []
        for result in my_cursor.stored_results():
            tmp.append(result.fetchall())
        res = tmp[0][0]['result']
        
        # my_cursor.execute(f"SELECT `db_project`.`login_user`(\"{self.username}\", \"{ppass}\") AS `login_result`;")
        # true_pass = list(my_cursor)[0]['login_result']
        if npass == "" or ppass=="":
            messagebox.showwarning("Failed", f"Your New Password Can\'t Be Empty!")
        elif res=="successfull":
            messagebox.showinfo("Success", f"Your password has been changed!")
        else:
            messagebox.showwarning("Failed", f"Your Previous Password Is Not Correct!")
