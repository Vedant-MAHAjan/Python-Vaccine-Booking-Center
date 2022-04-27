from tkinter import *
from tkinter import ttk

# import mysql as mysql
import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        self.var_fname = StringVar()
        #self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_passw = StringVar()
        self.var_blood = StringVar()
        self.var_addr = StringVar()

        # frame
        frame = Frame(self.root, bg="grey")
        frame.place(x=520, y=100, width=800, height=550)

        register_lb1 = Label(frame, text="Register", font=("times new roman", 20), bg="grey")
        register_lb1.place(x=325, y=20)

        # label and entry for row1
        fname = Label(frame, text="Name:", font=("arial", 16), bg="grey")
        fname.place(x=50, y=100)
        fname_entry = ttk.Entry(frame,textvariable=self.var_fname, font=("arial", 16))
        fname_entry.place(x=50, y=130, width=200)

        email = Label(frame, text="Email:", font=("arial", 16), bg="grey")
        email.place(x=370, y=100)
        self.email_entry = ttk.Entry(frame,textvariable=self.var_email, font=("arial", 16))
        self.email_entry.place(x=370, y=130, width=200)

        # row 2
        contact = Label(frame, text="Contact No:", font=("arial", 16), bg="grey")
        contact.place(x=50, y=170)
        self.contact_entry = ttk.Entry(frame,textvariable=self.var_contact, font=("arial", 16))
        self.contact_entry.place(x=50, y=200, width=200)

        passw = Label(frame, text="Password:", font=("arial", 16), bg="grey")
        passw.place(x=370, y=170)
        self.passw_entry = ttk.Entry(frame,textvariable=self.var_passw, show='*', font=("arial", 16))
        self.passw_entry.place(x=370, y=200, width=200)

        # #row3
        '''gender = Label(frame, text="Gender:", width=15, font=("arial", 16),bg="grey")
        gender.place(x=50, y=240)
        var = StringVar()
        ttk.Radiobutton(frame,padx=5, text="Male", variable=var, width=5,value=1).place(x=50, y=270)
        ttk.Radiobutton(frame,padx=10, text="Female", variable=var, width=5,value=2).place(x=80, y=270)
        ttk.Radiobutton(frame, padx=15,text="Others", variable=var, width=5,value=3).place(x=100, y=270)'''

        # row 4 for blood grp and address;
        blood = Label(frame, text="Blood Group:", font=("arial", 16), bg="grey")
        blood.place(x=50, y=310)
        self.combo_bg = ttk.Combobox(frame,textvariable=self.var_blood, font=("arial", 16), state="readonly")
        self.combo_bg["values"] = ("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")
        self.combo_bg.place(x=50, y=340)
        #self.textvariable=self.var_blood.current(0)'''

        addr = Label(frame, text="Address:", width=15, font=("arial", 16), bg="grey")
        addr.place(x=350, y=310)
        addr_entry = ttk.Entry(frame, textvariable=self.var_addr, font=("arial", 16))
        addr_entry.place(x=370, y=340, width=200, height=70)

        # register and login button
        b1 = Button(frame, text="Register", command=self.register_data, width=10, height=2, font=("Arial", 14),
                    bg="grey", fg="white")
        b1.place(x=100, y=450)

        b2 = Button(frame, text="Login", width=10, height=2, font=("Arial", 14), bg="grey", fg="white")
        b2.place(x=400, y=450)

    def register_bt(self):
        pass


    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_contact.get() == "":
            messagebox.showerror("Error", "All fields required")
    #elif self.var_passw.get() != self.var_confpass.get():
     #   messagebox.showerror("Confirm password should be same as entered password")
    #elif self.var_check.get() == 0:
     #   messagebox.showerror("Please agree to terms and conditions")
        else:
            #messagebox.showinfo("Registerted successfully")
            conn = mysql.connector.connect(host="localhost", user="root", password="hello", database="mini",
                                           auth_plugin='mysql_native_password')
            my_cursor = conn.cursor()
            #query = ("select * from register")
            #value = (self.var_email.get(),)
            #my_cursor.execute(query, value)
            #my_cursor.execute(query, val)

            #row = my_cursor.fetchone()
            #if row != None:
            #   messagebox.showerror("User already exists")

            my_cursor.execute("insert into insertdata values(%s,%s,%s,%s,%s)",
            (
            self.var_contact.get(),
            self.var_fname.get(),
            self.var_email.get(),
            self.var_passw.get(),
            self.var_blood.get()
            )
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")



if __name__ == '__main__':
    root = Tk()
    app = Register(root)
    root.mainloop()
