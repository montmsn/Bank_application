import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import mysql.connector

# Todo: connect your database
DB_project = mysql.connector.connect(
  host="",
  user="",
  password="",
  port=3306,
  database = ""
)
DB_project.autocommit = True
my_cursor = DB_project.cursor(dictionary=True)

class Acc_info(ttk.Frame):
    def __init__(self, master,username):
        super().__init__(master, padding=(10, 20))
        self.pack(fill=BOTH, expand=YES)
        self.username = username
        
        my_cursor.execute(f"SELECT UID from bank_user where username=\"{self.username}\";")
        uid = list(my_cursor)[0]['UID']
        args = (uid,)
        my_cursor.callproc("acc_info",args)
        tmp = []
        for result in my_cursor.stored_results():
            tmp.append(result.fetchall())
        accs = tmp[0]
        table_data = []
        for acc in accs:
            table_data.append((acc['ACCID'],acc['card_number'],acc['balance'],acc['cvv2'],acc['expire_date']))
        
        # table_data = [
        #     (12213, 14324, 4324, 323, "1402-32-23"),
        #     (897, 9898, 9, 89, "1399-87-90"),
        # ]
        tv = ttk.Treeview(
            master=master, columns=[0, 1, 2, 3, 4], show=HEADINGS, height=7
        )
        for row in table_data:
            tv.insert("", END, values=row)

        tv.selection_set("I001")
        tv.heading(0, text="ACCID")
        tv.heading(1, text="Card Number")
        tv.heading(2, text="Balance")
        tv.heading(3, text="CVV2")
        tv.heading(4, text="Expire Date")
        tv.column(0, anchor=CENTER)
        tv.column(1, anchor=CENTER)
        tv.column(2, anchor=CENTER)
        tv.column(3, anchor=CENTER)
        tv.column(4, anchor=CENTER)
        tv.pack(side=LEFT, anchor=NE)
