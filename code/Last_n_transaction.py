import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
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
username = "mon"
password = "1234"
my_cursor = DB_project.cursor(dictionary=True)


class Last_n_transaction(ttk.Frame):
    def __init__(self, master,username):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)
        self.username = username
       
        self.ACC = ttk.StringVar(value="")
        self.num = ttk.StringVar(value="")


        

        def subb():
            for item in tv.get_children():
                tv.delete(item)
            
            args = (int(self.ACC.get()),int(self.num.get()),)
            x = my_cursor.callproc("last_n_transactions",args)
            tmp = []
            for result in my_cursor.stored_results():
                tmp.append(result.fetchall())
            accs = tmp[0]
            table_data = []
            for acc in accs:
                table_data.append((acc['TID'],acc['date'],acc['amount'],acc['sender'],acc['reciever']))
            for row in table_data:
                tv.insert("", END, values=row)
            tv.pack(side=LEFT, anchor=NE)
        # self.ACC = 0
        # self.n = 3
        def subb2():
            for item in tv.get_children():
                tv.delete(item)
                
            sdate = date_start.entry.get()
            x = sdate.split("/")
            if len(x[0]) == 1:
                x[0] = "0" + x[0]
            if len(x[1]) == 1:
                x[1] = "0" + x[1]
            final_sdate = x[2] + "-" + x[0] + "-" + x[1]
            
            edate = date_end.entry.get()
            x = edate.split("/")
            if len(x[0]) == 1:
                x[0] = "0" + x[0]
            if len(x[1]) == 1:
                x[1] = "0" + x[1]
            final_edate = x[2] + "-" + x[0] + "-" + x[1]
                        
            args = (int(self.ACC.get()),final_sdate,final_edate,)
            x = my_cursor.callproc("transaction_by_date",args)
            tmp = []
            for result in my_cursor.stored_results():
                tmp.append(result.fetchall())
            accs = tmp[0]
            table_data = []
            for acc in accs:
                table_data.append((acc['TID'],acc['date'],acc['amount'],acc['sender'],acc['reciever']))
            for row in table_data:
                tv.insert("", END, values=row)
            tv.pack(side=LEFT, anchor=NE)
        
        
        # table_data = [
        #     (12213, "1402-32-23", 4324, 323, 76),
        #     (897, "1399-87-90", 9, 89, 43),
        # ]
        tv = ttk.Treeview(
            master=master, columns=[0, 1, 2, 3, 4], show=HEADINGS, height=7
        )
        

        # tv.selection_set("I001")
        tv.heading(0, text="TID")
        tv.heading(1, text="Date")
        tv.heading(2, text="Amount")
        tv.heading(3, text="Sender")
        tv.heading(4, text="Reciever")
        tv.column(0, anchor=CENTER)
        tv.column(1, anchor=CENTER)
        tv.column(2, anchor=CENTER)
        tv.column(3, anchor=CENTER)
        tv.column(4, anchor=CENTER)
        tv.pack(side=LEFT, anchor=NE)

        btn_group = ttk.Frame(master=master, padding=(10, 5))
        btn_group.pack(fill=X, side=LEFT)

        lbl = ttk.Label(btn_group, text="Account Number:")
        lbl.pack(side=TOP)

        ent = ttk.Entry(master=btn_group, textvariable=self.ACC)
        ent.pack(side=TOP, padx=5)
        lbl2 = ttk.Label(btn_group, text="Num Trans:")
        lbl2.pack(side=TOP)

        ent2 = ttk.Entry(master=btn_group, textvariable=self.num)
        ent2.pack(side=TOP, padx=5)
        bu = ttk.Button(
            master=btn_group,
            text="Submit",
            command=subb,
            bootstyle=SUCCESS,
        )
        bu.pack(fill=X, pady=5, side=TOP)
        
        btn_group = ttk.Frame(master=master, padding=(10, 5))
        btn_group.pack(fill=X, side=LEFT)

        lbl2 = ttk.Label(btn_group, text="Start Date:")
        lbl2.pack(side=TOP)

        date_start = tb.DateEntry(btn_group)
        date_start.pack(side=TOP, fill=X, padx=10)

        lbl2 = ttk.Label(btn_group, text="End Date:")
        lbl2.pack(side=TOP)

        date_end = tb.DateEntry(btn_group)
        date_end.pack(side=TOP, fill=X, padx=10)
        bu = ttk.Button(
            master=btn_group,
            text="Submit",
            command=subb2,
            bootstyle=SUCCESS,
        )
        bu.pack(fill=X, pady=5, side=TOP)
