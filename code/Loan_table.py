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

class Loan_table(ttk.Frame):
    def __init__(self, master,uesrname):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)
        self.username = uesrname
        
        args = (1111111112,)
        x = my_cursor.callproc("get_user_loans",args)
        tmp = []
        for result in my_cursor.stored_results():
            tmp.append(result.fetchall())
        accs = tmp[0] 
        table_data = []
        for acc in accs:
            table_data.append((acc['LID'],acc['ACCID'],acc['loan_score'],acc['loan_interest']))
            
        
        # table_data = [
        #     (12213, 14324, 4324, 323, "1402-32-23"),
        #     (897, 9898, 9, 89, "1399-87-90"),
        # ]
        tv = ttk.Treeview(master=master, columns=[0, 1, 2, 3], show=HEADINGS, height=10)
        for row in table_data:
            tv.insert("", END, values=row)

        # tv.selection_set("I001")
        tv.heading(0, text="LID")
        tv.heading(1, text="ACCID")
        tv.heading(2, text="Loan Score")
        tv.heading(3, text="Loan Interest")
        tv.column(0, anchor=CENTER)
        tv.column(1, anchor=CENTER)
        tv.column(2, anchor=CENTER)
        tv.column(3, anchor=CENTER)
        tv.pack(side=LEFT, anchor=NE,fill=BOTH,expand=YES)
