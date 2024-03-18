import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ChangePass import ChanePassword
from Acc_info import Acc_info
from Last_n_transaction import Last_n_transaction
from kavenegar import *
import mysql.connector
import random
from tkinter import messagebox
import smtplib
from Loan_table import Loan_table
from installment import installment


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

# Todo: add your api for sending OTP using sms, here we have used kavenegar.com
api = KavenegarAPI('')



# TODO
user_name = ", This is Bank DB"


def setup_demo(master,username):
    ZEN = """Beautiful is better than ugly."""

    root = ttk.Frame(master, padding=10)
    style = ttk.Style()
    theme_names = style.theme_names()

    theme_selection = ttk.Frame(root, padding=(10, 10, 10, 0))
    theme_selection.pack(fill=X, expand=YES)

    theme_selected = ttk.Label(
        master=theme_selection, text=f"Hello {user_name}", font="-size 24 -weight bold"
    )
    theme_selected.pack(side=LEFT)

    lbl = ttk.Label(theme_selection, text="Select a theme:")
    theme_cbo = ttk.Combobox(
        master=theme_selection,
        text=style.theme.name,
        values=theme_names,
    )
    theme_cbo.pack(padx=10, side=RIGHT)
    theme_cbo.current(theme_names.index(style.theme.name))
    lbl.pack(side=RIGHT)

    ttk.Separator(root).pack(fill=X, pady=10, padx=10)

    def change_theme(e):
        t = cbo.get()
        style.theme_use(t)
        theme_selected.configure(text=t)
        theme_cbo.selection_clear()
        default.focus_set()

    theme_cbo.bind("<<ComboboxSelected>>", change_theme)

    lframe = ttk.Frame(root, padding=5)
    lframe.pack(side=LEFT, fill=BOTH, expand=NO)

    rframe = ttk.Frame(root, padding=5)
    rframe.pack(side=RIGHT, fill=BOTH, expand=YES)

    color_group = ttk.Labelframe(master=lframe, text="Transaction Information")
    color_group.pack(fill=X, side=TOP)

    Last_n_transaction(color_group,username)

    # ChanePassword(rb_group,username)

    ttframe = ttk.Frame(lframe)
    ttframe.pack(pady=5, fill=X, side=TOP)

    color_group = ttk.Labelframe(master=ttframe, text="Account Information")
    color_group.pack(fill=X, side=LEFT,padx=5)

    Acc_info(color_group,username)

    rb_group = ttk.Labelframe(ttframe, text="Change Password", padding=10)
    rb_group.pack(fill=BOTH, pady=10, side=LEFT,expand=YES)

    ChanePassword(rb_group,username)

    rb_group = ttk.Labelframe(lframe, text="loan installments", padding=10)
    rb_group.pack(fill=X, pady=10, side=TOP)
    installment(rb_group)
    # text widget
    llfrr = ttk.Labelframe(master=lframe, text="Loans")
    llfrr.pack(fill=BOTH, side=LEFT)

    Loan_table(llfrr,username)
    
    lframe_inner = ttk.Labelframe(lframe, text="Show & Apply")
    lframe_inner.pack(fill=BOTH, expand=YES, padx=10, side=RIGHT)

    lbl = ttk.Label(lframe_inner, text="Account Number:")
    lbl.pack(side=TOP, pady=5)

    Loan_Acc = ttk.StringVar()
    ent = ttk.Entry(master=lframe_inner, textvariable=Loan_Acc)
    ent.pack(side=TOP, padx=5, pady=5)

    def show_loan():
        my_cursor.execute(f"SELECT `db_project`.`calculate_loan_score`({int(Loan_Acc.get())}) AS `loan_score`;")
        a = list(my_cursor)[0]['loan_score']
        Readyy.config(text=a)


    bu = ttk.Button(
        master=lframe_inner,
        text="Loan Score",
        command=show_loan,
        bootstyle=SUCCESS,
        width=18,
    )
    bu.pack(pady=5, side=TOP)

    def apply_loan():
        res = ""
        args = (int(Loan_Acc.get()), res,)
        x = my_cursor.callproc("get_loan",args)
        Readyy.config(text=x['get_loan_arg2'])


    bu = ttk.Button(
        master=lframe_inner,
        text="Apply Loan",
        command=apply_loan,
        bootstyle=SUCCESS,
        width=18,
    )
    bu.pack(pady=5, side=TOP)

    Readyy = ttk.Label(lframe_inner, text="Ready To Action")
    Readyy.pack(side=TOP)
    
    lframe_inner2 = ttk.Labelframe(lframe, text="Pay Last Payment")
    lframe_inner2.pack(fill=BOTH, expand=YES, padx=10, side=RIGHT)

    lbl5 = ttk.Label(lframe_inner2, text="Load ID:")
    lbl5.pack(side=TOP, pady=5)

    Loan_IDD = ttk.StringVar()
    ent5 = ttk.Entry(master=lframe_inner2, textvariable=Loan_IDD)
    ent5.pack(side=TOP, padx=5, pady=5)

    def Pay_last():
        res = ""
        args = (int(Loan_IDD.get()), res,)
        x = my_cursor.callproc("pay_last_payment",args)
        Readyy5.config(text=x['pay_last_payment_arg2'])
       

    bu = ttk.Button(
        master=lframe_inner2,
        text="Payyy!!!",
        command=Pay_last,
        bootstyle=SUCCESS,
        width=18,
    )
    bu.pack(pady=5, side=TOP)

    Readyy5 = ttk.Label(lframe_inner2, text="Ready To Action")
    Readyy5.pack(side=TOP)
    
    btn_group = ttk.Labelframe(master=rframe, text="Transit Money", padding=(10, 5))
    btn_group.pack(fill=X)

    menu = ttk.Menu(root)
    for i, t in enumerate(style.theme_names()):
        menu.add_radiobutton(label=t, value=i)

    lbl = ttk.Label(btn_group, text="Source Account:")
    lbl.pack(side=TOP)

    Tr_ACS = ttk.StringVar(value=0)
    ent = ttk.Entry(master=btn_group, textvariable=Tr_ACS)
    ent.pack(side=TOP, padx=5)

    lbl = ttk.Label(btn_group, text="Destination Account:")
    lbl.pack(side=TOP)

    Tr_ACD = ttk.StringVar(value=0)
    ent = ttk.Entry(master=btn_group, textvariable=Tr_ACD)
    ent.pack(side=TOP, padx=5)

    lbl = ttk.Label(btn_group, text="Amount:")
    lbl.pack(side=TOP)

    Tr_M = ttk.StringVar(value=0)
    ent = ttk.Entry(master=btn_group, textvariable=Tr_M)
    ent.pack(side=TOP, padx=5)

    lbl = ttk.Label(btn_group, text="OTP:")
    lbl.pack(side=TOP)

    Tr_OTP = ttk.StringVar(value=0)
    ent = ttk.Entry(master=btn_group, textvariable=Tr_OTP)
    ent.pack(side=TOP, padx=5)

    def email_OTP():
        my_cursor.execute(f"SELECT UID from bank_user where username=\"{username}\";")
        uid = list(my_cursor)[0]['UID']
        tmp = []
        args = (uid,)
        x = my_cursor.callproc("acc_info",args)
        for result in my_cursor.stored_results():
              tmp.append(result.fetchall())
        accs = tmp[0]  
        accs_email = {acc['card_number']:acc['email'] for acc in accs}
        
        otp_code = random.randrange(1000,10000)
        sc = str(Tr_ACS.get())
        my_cursor.execute(f"UPDATE card SET OTP={otp_code} where card_number=\"{sc}\";")
        
        # Todo: add your email info here as sender email, here we have used gmail
        gmail_user = ''
        gmail_app_password = ''
        sent_from = gmail_user
        # accs_email = accs_email[0]
        # print(accs_email)
        print(sc)
        # print(accs_email[sc])
        
        try:
            sent_to = [accs_email[sc]]
            # Todo: add your email info here as sender email, here we have used gmail
            gmail_user = ''
            gmail_app_password = ''

            sent_from = gmail_user
            sent_to = [accs_email[sc]]
            sent_subject = "Hey Friends!"
            sent_body = (f"Hey, what's up? friend!\n\nI hope you have been well!\n\nDashami,\nOTP:{otp_code}\n")

            email_text = """From: %sTo: %sSubject: %s %s""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

            print(sent_from, ", ".join(sent_to), sent_subject, sent_body)

            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_app_password)
                server.sendmail(sent_from, sent_to, email_text)
                server.close()

                print('Email sent!')
            except Exception as exception:
                print("Error: %s!\n\n" % exception)
            
        except:
            messagebox.showwarning("Login Success", f"dude! you can only trandfer moneey frmo your account :///")
        
        
        
        
        

    default = ttk.Button(
        master=btn_group, text="OTP to Email", width=19, bootstyle=(INFO, OUTLINE),command=email_OTP
    )
    default.pack(pady=5)
    default.focus_set()

    def sms_OTP():
        my_cursor.execute(f"SELECT UID from bank_user where username=\"{username}\";")
        uid = list(my_cursor)[0]['UID']
        tmp = []
        args = (uid,)
        x = my_cursor.callproc("acc_info",args)
        for result in my_cursor.stored_results():
              tmp.append(result.fetchall())
        accs = tmp[0]  
        accs_phone = {acc['card_number']:acc['phone_number'] for acc in accs} 
        # accs_phone = accs_phone[0]
        sc = str(Tr_ACS.get())
        otp_code = random.randrange(1000,10000)
        my_cursor.execute(f"UPDATE card SET OTP={otp_code} where card_number=\"{sc}\";")
        print(accs_phone)
        try:
            params = { 'sender' : '10008663', 'receptor': accs_phone[sc], 'message' : f'your OTP: {otp_code}' }
            response = api.sms_send(params)
        except:
            messagebox.showwarning("Login Success", f"dude! you can only trandfer moneey frmo your account :///")
    
    default = ttk.Button(
        master=btn_group, text="OTP to SMS", width=19, bootstyle=(INFO, OUTLINE),command=sms_OTP
    )
    default.pack(pady=5)
    default.focus_set()

    def transfer():
        my_cursor.execute(f"SELECT UID from bank_user where username=\"{username}\";")
        uid = list(my_cursor)[0]['UID']
        tmp = []
        args = (uid,)
        x = my_cursor.callproc("acc_info",args)
        for result in my_cursor.stored_results():
              tmp.append(result.fetchall())
        accs = tmp[0]  
        card_numbers = [acc['card_number'] for acc in accs] 
    
        sc = str(Tr_ACS.get())
        dc = str(Tr_ACD.get())
        amount = int(Tr_M.get())
        otp = int(Tr_OTP.get())
        my_cursor.execute(f"select OTP from card where card_number=\'{sc}\'")
        real_otp = list(my_cursor)[0]["OTP"] 
        if otp==real_otp:
            if sc not in card_numbers:
                messagebox.showwarning("Failed", f"Dadash mikhay as hesab digaran boland koni???!!!")
            else:
                res = ""
                args = (sc, dc, amount, res,)
                x = my_cursor.callproc("do_transaction",args)
                print(amount)
                if x['do_transaction_arg4']=='successful':
                    
                    messagebox.showinfo("Success", f"pool az hesabet parid raft...")
                else:
                    messagebox.showwarning("Failed", f"Haji hesabet dige inghadr pool nadare ke...")
        else:
            messagebox.showwarning("Failed", f"wrong OTP...")
            
                
        

    default = ttk.Button(master=btn_group, text="Transittt!",command=transfer)
    default.pack(fill=X, pady=5)
    default.focus_set()


    
        


    input_group = ttk.Labelframe(master=rframe, text="Suspend Account", padding=10)
    input_group.pack(fill=BOTH, pady=(10, 5), expand=YES)

    lbl = ttk.Label(input_group, text="Account Number:")
    lbl.pack(side=TOP)

    TRRRR = ttk.StringVar(value=0)
    ent = ttk.Entry(master=input_group, textvariable=TRRRR)
    ent.pack(side=TOP, padx=5)

    lbl = ttk.Label(input_group, text="Reason to Suspend:")
    lbl.pack(side=TOP, pady=5)

    txt = ttk.Text(master=input_group, height=5, width=24)
    txt.insert(END, ZEN)
    txt.pack(side=TOP, anchor=NW)

    def suspend():
        my_cursor.execute(f"SELECT UID from bank_user where username=\"{username}\";")
        uid = list(my_cursor)[0]['UID']
        tmp = []
        args = (uid,)
        x = my_cursor.callproc("acc_info",args)
        for result in my_cursor.stored_results():
              tmp.append(result.fetchall())
        accs = tmp[0]  
        accs = [acc['ACCID'] for acc in accs] 
        if int(TRRRR.get()) in accs:
            args = (int(TRRRR.get()),)
            my_cursor.callproc("suspend_acc",args)
            messagebox.showinfo("SUSPENDED","you have suspended")
        else:
            messagebox.showwarning("ERROR","you can only suspend your account")
    default = ttk.Button(master=input_group, text="Suspenddd!",command=suspend)
    default.pack(fill=X, pady=5)
    default.focus_set()
    
    cbo = ttk.Combobox(
        master=input_group,
        text=style.theme.name,
        values=theme_names,
        exportselection=False,
    )
    cbo.pack(fill=X, pady=5)
    cbo.current(theme_names.index(style.theme.name))
    
    return root


def dashboard(username):
    app = ttk.Window("ttkbootstrap widget demo", themename="superhero")

    bagel = setup_demo(app,username)
    bagel.pack(fill=BOTH, expand=YES)

    app.mainloop()

dashboard('mon')