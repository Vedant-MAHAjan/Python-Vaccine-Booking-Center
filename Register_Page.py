#MY REGISTER PAGE CODE
import subprocess
import sys
from tkinter import *
from tkinter import *
from tkinter import ttk
import mysql.connector

# import mysql as mysql
#import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("User Register")
        self.root.geometry("800x650+275+25")

        self.bg = ImageTk.PhotoImage(file="Reg_bg.png")
        lb_bg = Label(self.root, image=self.bg)
        lb_bg.place(x=0, y=0, relwidth=1, relheight=1)

        self.var_fname = StringVar()
        #self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_passw = StringVar()
        self.var_blood = StringVar()
        self.var_addr = StringVar()

        #Hover
        def changeOnHover(button, colorOnHover, colorOnLeave):
            # background on entering widget
            button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))

            # background color on leving widget
            button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

        # frame
        frame = Frame(self.root,bg="#5B5B5B")
        frame.place(x=15, y=100, width=420, height=540)

        #register text
        register_lb1 = Label(frame, text="User Register", font=("Open sans", 22, "bold"), bg="#5B5B5B",fg="white")
        register_lb1.place(x=130, y=20)

        # label and entry for row1
        fname = Label(frame, text="Name:", font=("arial", 16), bg="#5B5B5B",fg="white")
        fname.place(x=99, y=90)
        self.fname_entry = ttk.Entry(frame,textvariable=self.var_fname, font=("arial", 16))
        self.fname_entry.place(x=170, y=90, width=200)

        email = Label(frame, text="Email:", font=("arial", 16), bg="#5B5B5B",fg="white")
        email.place(x=103, y=140)
        self.email_entry = ttk.Entry(frame,textvariable=self.var_email, font=("arial", 16))
        self.email_entry.place(x=170, y=140, width=200)

        passw = Label(frame, text="Password:", font=("arial", 16), bg="#5B5B5B",fg="white")
        passw.place(x=63, y=190)
        self.passw_entry = ttk.Entry(frame,textvariable=self.var_passw, show='*', font=("arial", 16))
        self.passw_entry.place(x=170, y=190, width=200)

        # row 2
        contact = Label(frame, text="Contact No:", font=("arial", 16), bg="#5B5B5B",fg="white")
        contact.place(x=50, y=240)
        self.contact_entry = ttk.Entry(frame,textvariable=self.var_contact, font=("arial", 16))
        self.contact_entry.place(x=170, y=240, width=200)
        #self.contact_v = ttk.Entry(frame, textvariable=self.var_contact, font=("arial", 16))
        #self.contact_v.place(x=170, y=270, width=200,height=20)

        # #row3
        gender = Label(frame, text="Gender:", font=("arial", 16),bg="#5B5B5B",fg="white")

        s = ttk.Style()  # Creating style element
        s.configure('Wild.TRadiobutton', background="#5B5B5B", foreground='white',font=("arial", 11))

        gender.place(x=88, y=285)
        var = IntVar()
        self.r1 = ttk.Radiobutton(frame, text="Male", variable=var, value=1,style = 'Wild.TRadiobutton')
        self.r1.place(x=172, y=290)
        self.r2= ttk.Radiobutton(frame, text="Female",  variable=var, value=2,style = 'Wild.TRadiobutton')
        self.r2.place(x=235, y=290)
        self.r3 = ttk.Radiobutton(frame, text="Other",variable=var, value=3,style = 'Wild.TRadiobutton')
        self.r3.place(x=320, y=290)

        # row 4 for blood grp and address;
        blood = Label(frame, text="Blood Group:", font=("arial", 16), bg="#5B5B5B",fg="white")
        blood.place(x=38, y=340)
        self.combo_bg = ttk.Combobox(frame,textvariable=self.var_blood,width=15, font=("arial", 16), state="readonly")
        self.combo_bg["values"] = ("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")
        self.combo_bg.place(x=170, y=340)
        #self.textvariable=self.var_blood.current(0)'''

        addr = Label(frame, text="Address:",font=("arial", 16), bg="#5B5B5B",fg="white")
        addr.place(x=78, y=400)
        self.addr_entry = ttk.Entry(frame, textvariable=self.var_addr, font=("arial", 16))
        self.addr_entry.place(x=170, y=390, width=200, height=70)

        # register and login button
        b1 = Button(frame, text="Register", command=self.register_data, width=10, height=1, font=("Arial", 14),
                    bg="#CFCFCF", fg="black", activeforeground="black", activebackground="#FFDE59",)
        b1.place(x=225, y=480)
        changeOnHover(b1, "#6BC145", "#CFCFCF")

        b2 = Button(frame, text="Back", width=9, height=1, font=("Arial", 14), bg="#CFCFCF", fg="black",command=lambda :UL_call(root))
        b2.place(x=80, y=480)
        changeOnHover(b2, "#FF5757", "#CFCFCF")

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

            my_cursor.execute("insert into register values(%s,%s,%s,%s,%s)",
            (
            self.var_contact.get(),
            self.var_fname.get(),
            self.var_email.get(),
            self.var_passw.get(),
            self.var_blood.get(),
            #self.var_addr().get()
            )
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")


def UL_call(root):
   root.destroy()
   #subprocess('python login.py')
   subprocess.run([sys.executable, 'Home_Page.py'])


if __name__ == '__main__':
    root = Tk()
    app = Register(root)
    root.mainloop()

    # take this register class to home file and paste at bottom

    # def database():

