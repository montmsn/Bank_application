import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageSequence
from pathlib import Path
from itertools import cycle
import animated_gif
import mysql.connector
from dashboard import dashboard

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

# Create the main window
app = ttk.Window(themename="superhero")
app.title("Bank")
app.iconbitmap("piggy-bank.ico")
app.geometry("840x440")

# Images
show_img = Image.open("hide.png")
show_img_resized = show_img.resize((24, 24), Image.BICUBIC)
show_icon = ImageTk.PhotoImage(show_img_resized)

hide_img = Image.open("show.png")
hide_img_resized = hide_img.resize((24, 24), Image.BICUBIC)
hide_icon = ImageTk.PhotoImage(hide_img_resized)

# Create a frame for the login fields
rframe = ttk.Frame(app, padding=20)
rframe.pack(side=LEFT, fill=BOTH, expand=YES)


def login():
    username = username_entry.get()
    password = password_entry.get()
    my_cursor.execute(f"SELECT `db_project`.`login_user`(\"{username}\", \"{password}\") AS `login_result`;")
    if list(my_cursor)[0]['login_result']:
        # messagebox.showinfo("Login Success", f"Welcome to the Matrix, dear {}!")
        my_cursor.execute(f"SELECT first_name FROM bank_user where username=\'{username}\'")
        fname =list(my_cursor)[0]['first_name']
        messagebox.showinfo("Login Success", f"Welcome To Our Bank, dear {fname}!")
        app.destroy()
        # dashboard(username)
        app.quit()
        animated_gif.strat_animate(username)
        # dashboard(username)

    else:
        messagebox.showwarning(
            "Login Failed", "wrong username or password, dude!"
        )


def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        password_toggle_button.config(image=show_icon)
    else:
        password_entry.config(show="")
        password_toggle_button.config(image=hide_icon)


input_group = ttk.Labelframe(master=rframe, text="Log in to your account", padding=10)
input_group.pack(fill=BOTH, pady=(0, 5), side=LEFT, padx=10)

# username_label = ttk.Label(app, text="Username:")
username_label = ttk.Label(input_group, text="Username:")
username_label.pack(pady=10)
username_entry = ttk.Entry(input_group)
username_entry.pack(pady=10, ipadx=25)

# Password field
password_label = ttk.Label(input_group, text="Password:")
password_label.pack(pady=10)

container = ttk.Frame(input_group)
container.pack(pady=(0, 5), expand=True)

# Password field
password_entry = ttk.Entry(container, show="*")
password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Checkbox to show/hide password
password_toggle_button = ttk.Button(
    container,
    image=show_icon,
    command=toggle_password,
    bootstyle="outline-toolbutton",
)
password_toggle_button.pack(side=tk.LEFT, padx=(5, 0))


container2 = ttk.Frame(input_group)
container2.pack(pady=(0, 5), expand=True)

# Login button
login_button = ttk.Button(
    container2, text="Login", command=login, bootstyle="success", width=10
)
login_button.pack(pady=20, side=tk.LEFT, fill=tk.X, expand=True)

signup_button = ttk.Button(
    container2, text="Sign-up", command=login, bootstyle="danger", width=10
)
signup_button.pack(pady=20, side=tk.LEFT, padx=(5, 0))


about_group = ttk.Labelframe(master=rframe, text="About us", padding=10)
about_group.pack(fill=BOTH, pady=(0, 5), expand=YES)

about_pic = Image.open("about.jpeg")
show_img_resized = about_pic.resize((500, 200), Image.BICUBIC)
about_pic = ImageTk.PhotoImage(show_img_resized)

Welcome_label = ttk.Label(
    about_group, text="Welcome to our bank", bootstyle="danger", image=about_pic
)
Welcome_label.pack()

nb = ttk.Notebook(about_group)
nb.pack(side=LEFT, padx=(10, 0), expand=YES, fill=BOTH)
nb_text = "We Are God Of Database.\nEnjoy The Best App Ever"
nb.add(ttk.Label(nb, text=nb_text), text="About Us", sticky=NW)
nb.add(
    child=ttk.Label(nb, text="Mohammad Saleh Naseh (Mon)\nAli TamiziFar"),
    text="Creators",
    sticky=NW,
)

app.mainloop()
