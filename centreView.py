import subprocess
import sys
from tkinter import *
from tkinter import ttk, messagebox
import tkinter.messagebox
from tkinter.ttk import Treeview
import mysql.connector

import smtplib
import imghdr
from email.message import EmailMessage

'''Main_Frame = Frame(bg='#545454')
Main_Frame.grid()'''


class Fee():
    #patient_rec: Treeview

    def __init__(self, master):
        self.master = master
        self.master.title('Center Management')

        def Tuple(event):
            try:
                global st
                index = self.list.curselection()[0]
                st = self.list.get(index)

                '''self.recpt_entry.delete(0, END)
                self.recpt_entry.insert(END, st[1])
                self.name_entry.delete(0, END)
                self.name_entry.insert(END, st[2])
                self.admsn_entry.delete(0, END)
                self.admsn_entry.insert(END, st[3])
                self.Date_entry.delete(0, END)
                self.Date_entry.insert(END, st[4])
                self.branch_entry.delete(0, END)
                self.branch_entry.insert(END, st[5])
                self.sem_entry.delete(0, END)
                self.sem_entry.insert(END, st[6])
                self.total_entry.delete(0, END)
                self.total_entry.insert(END, st[7])
                self.paid_entry.delete(0, END)
                self.paid_entry.insert(END, st[8])
                self.due_entry.delete(0, END)
                self.due_entry.insert(END, st[9])'''
            except IndexError:
                pass

        # ==================================================Variables=================================================

        self.cid = DoubleVar()
        self.name = StringVar()
        self.email = StringVar()
        self.centre = StringVar()
        self.result = StringVar()

        Title_Frame = LabelFrame(master, width=1350, height=100, bg='#5b5b5b', relief='ridge', bd=15)
        Title_Frame.pack(side=TOP)

        lblTitle = Label(Title_Frame, font=('arial', 40, 'bold'), fg='white', text='PATIENT DETAILS', bg='#5b5b5b',
                         padx=13)
        lblTitle.grid(padx=400)

        Data_Frame = Frame(master, width=1350, height=350, bg='#5b5b5b', relief='ridge', bd=1)
        Data_Frame.pack(side=TOP, padx=10, pady=5)

        Frame_1 = LabelFrame(Data_Frame, width=850, height=350, bg='#5b5b5b', relief='ridge', bd=8, text='Informations',
                             fg='white', font=('arial', 15, 'bold'))
        Frame_1.pack(side=LEFT, padx=10, pady=5)

        List_Frame = Frame(master, width=1350, height=350, bg='#5b5b5b', relief='ridge', bd=15)
        List_Frame.pack(side=TOP, padx=15, pady=7)

        # ===================================================Labels================================================

        self.cid_label = Label(Frame_1, text='Name: ', font=(
            'arial', 14, 'bold'), bg='#5b5b5b', fg='white')
        self.cid_label.grid(row=0, column=0, padx=15, sticky=W)

        self.name_label = Label(Frame_1, text='Email: ', font=(
            'arial', 14, 'bold'), bg='#5b5b5b', fg='white')
        self.name_label.grid(row=1, column=0, padx=15, sticky=W)

        self.email_label = Label(Frame_1, text='Centre: ', font=(
            'arial', 14, 'bold'), bg='#5b5b5b', fg='white')
        self.email_label.grid(row=2, column=0, padx=15, sticky=W)

        self.centre_label = Label(Frame_1, text='Health ID: ', font=(
            'arial', 14, 'bold'), bg='#5b5b5b', fg='white')
        self.centre_label.grid(row=1, column=2, padx=15, sticky=W)

        # self.blood_label = Label(Frame_1, text='Blood Group: ', font=('arial', 14, 'bold'), bg='#666666', fg='white')
        # self.blood_label.grid(row=0, column=2, padx=5, sticky=W)

        self.result_label = Label(Frame_1, text='Result: ', font=(
            'arial', 14, 'bold'), bg='#5b5b5b', fg='white')
        self.result_label.grid(row=0, column=2, padx=15, sticky=W)

        # ==================================================Entries=================================================
        # self.var_1 = DoubleVar(Frame_1)
        # d1 = datetime.date.today()
        # self.date.set(d1)

        self.cid_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.cid)
        self.cid_entry.grid(row=1, column=3, padx=15, pady=10)

        self.name_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.name)
        self.name_entry.grid(row=0, column=1, padx=15, pady=10)

        self.email_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.email)
        self.email_entry.grid(row=1, column=1, padx=15, pady=10)

        self.centre_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.centre)
        self.centre_entry.grid(row=2, column=1, padx=15, pady=10)

        # self.blood_entry = Entry(Frame_1, font=('arial', 14), width=15)
        # self.blood_entry.grid(row=0, column=3, padx=50, pady=10)

        self.result_entry = ttk.Combobox(Frame_1, values=('Positive', 'Negative'), font=('arial', 14),
                                         textvariable=self.result)
        '''self.result_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.result)'''
        self.result_entry.grid(row=0, column=3, padx=15, pady=10)

        btnUpdate = Button(Frame_1,command=self.update_info, text='UPDATE', font=(
            'arial', 14, 'bold'), width=10)
        btnUpdate.grid(row=0, column=4, padx=5, pady=5)

        # btnSearch = Button(Frame_1,command = self.search_records, text='SEARCH', font=(
        #     'arial', 14, 'bold'), width=10)
        # btnSearch.grid(row=0, column=5, padx=5, pady=5)

        btnDelete = Button(Frame_1,command = self.delete, text='DELETE', font=(
            'arial', 14, 'bold'), width=10)
        btnDelete.grid(row=0, column=6, padx=5, pady=5)

        btnDahisar = Button(Frame_1, command=self.show_Dahisar, text='DAHISAR', font=(
            'arial', 14, 'bold'), width=10)
        btnDahisar.grid(row=1, column=4, padx=5, pady=5)

        btnBorivali = Button(Frame_1, text='BORIVALI', font=(
            'arial', 14, 'bold'), width=10, command=self.show_Borivali)
        btnBorivali.grid(row=1, column=6, padx=5, pady=5)

        btnKandivali = Button(Frame_1, text='KANDIVALI', font=(
            'arial', 14, 'bold'), width=10, command=self.show_Kandivali)
        btnKandivali.grid(row=1, column=5, padx=5, pady=5)

        s_rep_btn= Button(Frame_1, text='SEND', font=(
            'arial', 14, 'bold'), width=10, command=lambda: self.send_report(root))
        s_rep_btn.grid(row=0, column=5, padx=5, pady=5)

        btnExit = Button(Frame_1, text='EXIT', font=(
            'arial', 14, 'bold'), width=10, command=lambda: UL_call(root))
        btnExit.grid(row=2, column=5, padx=5, pady=5)

        # =============================================List box and scrollbar===========================================
        sb = Scrollbar(List_Frame)
        sb.grid(row=0, column=1, sticky='ns')

        self.list = Listbox(List_Frame, font=('arial', 13, 'bold'), width=140, height=12)
        self.list.bind('<<ListboxSelect>>', Tuple)
        self.list.grid(row=0, column=0, pady=1)
        sb.config(command=self.list.yview)

        self.patient_rec = ttk.Treeview(List_Frame, columns=("cid","name", "mail", "center","result"))
        # scroll_x.pack(side=BOTTOM, fill = X)
        # scroll_y.pack(side=BOTTOM, fill = X)

        self.patient_rec.heading("cid", text="Health ID")
        self.patient_rec.heading("name", text="Name")
        self.patient_rec.heading("mail", text="Mail")
        self.patient_rec.heading("center", text="Center")
        # self.patient_rec.heading("test", text="Test")
        # self.patient_rec.heading("sample", text="Sample")
        self.patient_rec.heading("result", text="Result")

        self.patient_rec['show'] = 'headings'

        self.patient_rec.column("cid", width=250)
        self.patient_rec.column("name", width=250)
        self.patient_rec.column("mail", width=250)
        self.patient_rec.column("center", width=250)
        # self.patient_rec.column("test", width=150)
        # self.patient_rec.column("sample", width=150)
        self.patient_rec.column("result", width=250)

        #self.patient_rec.pack(fill=BOTH,expand=1)
        self.patient_rec.grid(row=0, column=0)
       # self.patient_rec.bind("<ButtonRelease-1>",self.fill_info)

        def show_details():
            conn = mysql.connector.connect(host="localhost", user="root", password="hello", database="mini",
                                           auth_plugin='mysql_native_password')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from book_table")
            rows = my_cursor.fetchall()
            for row in rows:
                self.patient_rec.insert('',END,values = row)
            conn.commit()
            conn.close()

        show_details()

        def fill_info(ev):
            viewInfo = self.patient_rec.focus()
            fill_data = self.patient_rec.item(viewInfo)
            row = fill_data['values']
            self.cid.set(row[0])
            self.name.set(row[1])
            self.email.set(row[2])
            self.centre.set(row[3])
            self.result.set(row[4])

        self.patient_rec.bind("<ButtonRelease-1>", fill_info)

    def update_info(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="hello", database="mini",
                                           auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("update book_table set name=%s,email=%s,centre=%s,result=%s where pin=%s",
        (self.name_entry.get(),self.email_entry.get(),
             self.centre_entry.get(),self.result_entry.get(),self.cid_entry.get()))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Updated Successfully")


    def delete(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="hello", database="mini",
                                       auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("delete from book_table where pin=%s and name=%s",(self.cid_entry.get(),self.name_entry.get()))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Deleted Successfully")


    def show_Dahisar(self):
        self.patient_rec.delete(*self.patient_rec.get_children())

        conn = mysql.connector.connect(host="localhost", user="root", password="hello", database="mini",
                                       auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from book_table where centre='Dahisar'")
        rows = my_cursor.fetchall()
        for row in rows:
            self.patient_rec.insert('', END, values=row)
        conn.commit()
        conn.close()

    def show_Borivali(self):
        self.patient_rec.delete(*self.patient_rec.get_children())

        conn = mysql.connector.connect(host="localhost", user="root", password="hello", database="mini",
                                       auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from book_table where centre='Borivali'")
        rows = my_cursor.fetchall()
        for row in rows:
            self.patient_rec.insert('', END, values=row)
        conn.commit()
        conn.close()

    def show_Kandivali(self):
        self.patient_rec.delete(*self.patient_rec.get_children())

        conn = mysql.connector.connect(host="localhost", user="root", password="hello", database="mini",
                                       auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from book_table where centre='Kandivali'")
        rows = my_cursor.fetchall()
        for row in rows:
            self.patient_rec.insert('', END, values=row)
        conn.commit()
        conn.close()



    def send_report(self,root):

        sender_email = "care19centre@gmail.com"

        password = "care19_python"

        msg = EmailMessage()
        msg['Subject'] = 'Covid Report'
        msg['From'] = sender_email
        msg['To'] = self.email_entry.get()
        msg.set_content(f'Thank You {self.name.get()} for contacting Care19')

        with open('covid report.png', 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name

        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(msg)
        messagebox.showinfo("Success","Report Sent Successfully")


def UL_call(root):
    root.destroy()
    # subprocess('python login.py')
    subprocess.run([sys.executable, 'login.py'])
    pass


root = Tk()
obj = Fee(root)
root.mainloop()




