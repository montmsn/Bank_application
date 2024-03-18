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
my_cursor = DB_project.cursor(dictionary=True)


class installment(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)

        self.LL = ttk.IntVar(value=0)

        def subb():
            
            for item in tv.get_children():
                tv.delete(item)
            
            args = (int(self.LL.get()),)
            x = my_cursor.callproc("loan_payments",args)
            tmp = []
            for result in my_cursor.stored_results():
                tmp.append(result.fetchall())
            accs = tmp[0]
            table_data = []
            for acc in accs:
                table_data.append((acc['payID'],acc['LID'],acc['payment_amount'],acc['settled']))
            for row in table_data:
                tv.insert("", END, values=row)
            tv.pack(side=LEFT, anchor=NE)
            
            
            
            
            # int(self.LL.get())
            # pass

        # table_data = [
        #     (12213, "1402-32-23", 4324, 323, 76),
        #     (897, "1399-87-90", 9, 89, 43),
        # ]
        tv = ttk.Treeview(master=master, columns=[0, 1, 2, 3], show=HEADINGS, height=5)
        # for row in table_data:
        #     tv.insert("", END, values=row)

        # tv.selection_set("I001")
        tv.heading(0, text="PayID")
        tv.heading(1, text="LID")
        tv.heading(2, text="Payment Amount")
        tv.heading(3, text="Setteled")
        tv.column(0, anchor=CENTER)
        tv.column(1, anchor=CENTER)
        tv.column(2, anchor=CENTER)
        tv.column(3, anchor=CENTER)
        tv.pack(side=LEFT, anchor=NE)

        btn_group = ttk.Frame(master=master, padding=(10, 5))
        btn_group.pack(fill=X, side=LEFT)

        lbl = ttk.Label(btn_group, text="Loan Number:")
        lbl.pack(side=TOP)

        ent = ttk.Entry(master=btn_group, textvariable=self.LL)
        ent.pack(side=TOP, padx=5)

        bu = ttk.Button(
            master=btn_group,
            text="Installments",
            command=subb,
            bootstyle=SUCCESS,
        )
        bu.pack(fill=X, pady=5, side=TOP)
