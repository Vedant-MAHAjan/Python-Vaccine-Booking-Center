import tkinter as tk
from tkinter import ttk
#from tkinter import *
#from login import *
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
#from atexit import register
#from tkinter import font
from tkinter import messagebox


def Home_page():
   abc= Tk()
   abc.title("Home Page")
   abc.geometry("700x500")
   tabControl = ttk.Notebook(abc)

   tab1 = ttk.Frame(tabControl)
   tab2 = ttk.Frame(tabControl)

   tabControl.add(tab1, text='Home')
   tabControl.add(tab2, text='About Us')
   tabControl.pack(expand=1, fill="both")

   # root.iconbitmap("F:\\Study M\\Experiments\\Mini Project\\Pictures\\Home_page.png")

   global home_img
   home_img = ImageTk.PhotoImage(Image.open("Home_page.png"))
   Tab_label1 = ttk.Label(tab1, image=home_img)
   Tab_label1.pack()

   global abt_us_img
   abt_us_img = ImageTk.PhotoImage(Image.open("About_us.png"))
   Tan_label2 = ttk.Label(tab2, image=abt_us_img)
   Tan_label2.pack()

   def changeOnHover(button, colorOnHover, colorOnLeave):
       # background on entering widget
       button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))

       # background color on leving widget
       button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

   UR_b = tk.Button(tab1, text="User Register", background="#CFCFCF", activebackground="#6BC145",
                    command=lambda: UR_call(root))
   UR_b.place(x=140, y=420, height=35, width=100)
   changeOnHover(UR_b, "#FFDE59", "#CFCFCF")

   UL_b = tk.Button(tab1, text="User Login", background="#CFCFCF", activebackground="#6BC145",
                    command=lambda: UL_call(root))
   UL_b.place(x=315, y=420, height=35, width=100)
   changeOnHover(UL_b, "#FFDE59", "#CFCFCF")

   CL_b = tk.Button(tab1, text="Centre Login", background="#CFCFCF", activebackground="#6BC145",
                    command=lambda: CL_call(root))
   CL_b.place(x=500, y=420, height=35, width=100)
   changeOnHover(CL_b, "#FFDE59", "#CFCFCF")


'''def login_window(self):
   self.new_window = Toplevel(self.root)
   self.app = Login_window(self.new_window)'''


# register page
def UR_call(root):
   root.destroy()
   link_register()


def link_register():
   def get_data():
       global data
       data = Tk()
       data.title("User Register")
       data.geometry("800x650+275+25")

       data.bg = ImageTk.PhotoImage(file="Reg_bg.png")
       lb_bg = Label(data, image=data.bg)
       lb_bg.place(x=0, y=0, relwidth=1, relheight=1)

       data.var_fname = StringVar()
       # data.var_lname = StringVar()
       data.var_contact = StringVar()
       data.var_email = StringVar()
       data.var_passw = StringVar()
       data.var_blood = StringVar()
       data.var_addr = StringVar()
       data.var_gender = StringVar()


       # Hover
       def changeOnHover(button, colorOnHover, colorOnLeave):
           # background on entering widget
           button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))

           # background color on leving widget
           button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

       # frame
       frame = Frame(data, bg="#5B5B5B")
       frame.place(x=15, y=100, width=420, height=540)

       # register text
       register_lb1 = Label(frame, text="User Register", font=("Open sans", 22, "bold"), bg="#5B5B5B", fg="white")
       register_lb1.place(x=130, y=20)

       # label and entry for row1
       fname = Label(frame, text="Name:", font=("arial", 16), bg="#5B5B5B", fg="white")
       fname.place(x=99, y=90)
       fname_entry = ttk.Entry(frame, textvariable=data.var_fname, font=("arial", 16))
       fname_entry.place(x=170, y=90, width=200)

       email = Label(frame, text="Email:", font=("arial", 16), bg="#5B5B5B", fg="white")
       email.place(x=103, y=140)
       data.email_entry = ttk.Entry(frame, textvariable=data.var_email, font=("arial", 16))
       data.email_entry.place(x=170, y=140, width=200)

       passw = Label(frame, text="Password:", font=("arial", 16), bg="#5B5B5B", fg="white")
       passw.place(x=63, y=190)
       data.passw_entry = ttk.Entry(frame, textvariable=data.var_passw, show='*', font=("arial", 16))
       data.passw_entry.place(x=170, y=190, width=200)

       # row 2
       contact = Label(frame, text="Contact No:", font=("arial", 16), bg="#5B5B5B", fg="white")
       contact.place(x=50, y=240)
       data.contact_entry = ttk.Entry(frame, textvariable=data.var_contact, font=("arial", 16))
       data.contact_entry.place(x=170, y=240, width=200)
       # data.contact_v = ttk.Entry(frame, textvariable=data.var_contact, font=("arial", 16))
       # data.contact_v.place(x=170, y=270, width=200,height=20)

       # #row3
       gender = Label(frame, text="Gender:", font=("arial", 16), bg="#5B5B5B", fg="white")

       s = ttk.Style()  # Creating style element
       s.configure('Wild.TRadiobutton', background="#5B5B5B", foreground='white', font=("arial", 11))

       gender.place(x=88, y=285)
       var = IntVar()
       data.r1 = ttk.Radiobutton(frame, text="Male", variable=var, value=1, style='Wild.TRadiobutton')
       data.r1.place(x=172, y=290)
       data.r2 = ttk.Radiobutton(frame, text="Female", variable=var, value=2, style='Wild.TRadiobutton')
       data.r2.place(x=235, y=290)
       data.r3 = ttk.Radiobutton(frame, text="Other", variable=var, value=3, style='Wild.TRadiobutton')
       data.r3.place(x=320, y=290)

       # row 4 for blood grp and address;
       blood = Label(frame, text="Blood Group:", font=("arial", 16), bg="#5B5B5B", fg="white")
       blood.place(x=38, y=340)
       data.combo_bg = ttk.Combobox(frame, textvariable=data.var_blood, width=15, font=("arial", 16), state="readonly")
       data.combo_bg["values"] = ("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")
       data.combo_bg.place(x=170, y=340)
       # data.textvariable=data.var_blood.current(0)'''

       addr = Label(frame, text="Address:", font=("arial", 16), bg="#5B5B5B", fg="white")
       addr.place(x=78, y=400)
       addr_entry = ttk.Entry(frame, textvariable=data.var_addr, font=("arial", 16))
       addr_entry.place(x=170, y=390, width=200, height=70)

       # register and login button
       b1 = Button(frame, text="Register", command=register_data, width=10, height=1, font=("Arial", 14),
                   bg="#CFCFCF", fg="black", activeforeground="black", activebackground="#FFDE59")
       b1.place(x=225, y=480)
       changeOnHover(b1, "#6BC145", "#CFCFCF")

       b2 = Button(frame, text="Back", width=9, height=1, font=("Arial", 14), bg="#CFCFCF", fg="black")
       b2.place(x=80, y=480)
       changeOnHover(b2, "#FF5757", "#CFCFCF")

   def register_data():
       if data.var_fname.get() == "" or data.var_email.get() == "" or data.var_contact.get() == "":
           messagebox.showerror("Error", "All fields required")
       # elif data.var_passw.get() != data.var_confpass.get():
       #   messagebox.showerror("Confirm password should be same as entered password")
       # elif data.var_check.get() == 0:
       #   messagebox.showerror("Please agree to terms and conditions")
       else:
           # messagebox.showinfo("Registerted successfully")
           conn = mysql.connector.connect(host="localhost", user="root", password="hello", database="mini",
                                          auth_plugin='mysql_native_password')
           my_cursor = conn.cursor()
           # query = ("select * from register")
           # value = (data.var_email.get(),)
           # my_cursor.execute(query, value)
           # my_cursor.execute(query, val)

           # row = my_cursor.fetchone()
           # if row != None:
           #   messagebox.showerror("User already exists")

           my_cursor.execute("insert into insertdata values(%s,%s,%s,%s,%s)",
                             (
                                 data.var_contact.get(),
                                 data.var_fname.get(),
                                 data.var_email.get(),
                                 data.var_passw.get(),
                                 data.var_blood.get(),
                                 data.var_gender()
                             )
                             )
           conn.commit()
           conn.close()
           messagebox.showinfo("Success", "Registered Successfully")

   get_data()


def UL_call(root):
   root.destroy()
   play()


# patient login link
def play():
   def patient_login():
       # root = root
       global patient
       patient = Tk()
       patient.title("User Login")
       patient.geometry("700x500")

       patient.bg = ImageTk.PhotoImage(file="User_login.png")
       lbl_bg = Label(patient, image=patient.bg)
       lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

       # Frame
       frame = Frame(patient, bg="#5B5B5B")
       frame.place(x=360, y=120, width=330, height=350)

       username = lbl = Label(frame, text="User Login", font=("Open sans", 22, "bold"), fg="white", bg="#5B5B5B")
       username.place(x=105, y=25)

       # user text field
       global txtuser
       txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
       txtuser.place(x=85, y=110, width=225, height=28)

       # password = lb2 = Label(frame, text="Password", font=("times new roman", 20, "bold"), fg="black", bg="skyblue")
       # password.place(x=50, y=215)
       global txtpass
       txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
       txtpass.place(x=85, y=180, width=225, height=28)

       img2 = Image.open("username_icon.png")
       img2 = img2.resize((40, 40), Image.ANTIALIAS)
       patient.photoimage2 = ImageTk.PhotoImage(img2)
       lblimg1 = Label(image=patient.photoimage2, bg="skyblue", borderwidth=0)
       lblimg1.place(x=390, y=220, width=40, height=40)

       img3 = Image.open("pass_icon.png")
       img3 = img3.resize((40, 40), Image.ANTIALIAS)
       patient.photoimage1 = ImageTk.PhotoImage(img3)
       lblimg1 = Label(image=patient.photoimage1, bg="skyblue", borderwidth=0)
       lblimg1.place(x=390, y=290, width=40, height=40)

       # **Hover
       def changeOnHover(button, colorOnHover, colorOnLeave):
           # background on entering widget
           button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))

           # background color on leving widget
           button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

           # **

       loginbtn = Button(frame, command=login, text="Login", font=("times new roman", 15, "bold"), bd=3,
                         relief=RIDGE, bg="#CFCFCF", activeforeground="black", activebackground="#FFDE59")
       loginbtn.place(x=120, y=240, width=125, height=35)
       changeOnHover(loginbtn, "#6BC145", "#CFCFCF")

       hpbtn = Button(frame, text="Home Page", font=("times new roman", 15, "bold"), borderwidth=0,
                      bg="#CFCFCF", activeforeground="white", activebackground="#FF5757",command=lambda :Home_page())
       hpbtn.place(x=120, y=290, width=125, height=35)
       changeOnHover(hpbtn, "#5CE1E6", "#CFCFCF")

   # database patient login
   def login():
       if txtuser.get() == "" or txtpass.get() == "":
           messagebox.showerror("Error", "All fields required")
       elif txtuser.get() == "abc123" and txtpass.get() == "abc123":
           messagebox.showinfo("Success", "Welcome to Care 19")
       else:
           conn = mysql.connector.connect(host="localhost", user="root", password="hello", database="mini",
                                          auth_plugin='mysql_native_password')
           my_cursor = conn.cursor()
           my_cursor.execute("select * from insertdata where email=%s and passw=%s",
                             (txtuser.get(), txtpass.get()))

           row = my_cursor.fetchone()
           if row == None:
               messagebox.showerror("Error", "Invalid username or password")
           else:
               '''open_main = messagebox.askyesno()
               new_window = Toplevel(new_window)
               self.app = Hospital(self.new_window)'''
               messagebox.showinfo("Success", "Welcome to the dashboard")

   patient_login()
   # login()


# centre login function
def CL_call(root):
   root.destroy()
   enjoy()


# centre login function
def enjoy():
   def login_Form():
       global screen
       screen = Tk()
       screen.title("Centre Login")
       screen.geometry("700x500+350+100")

       screen.bg = ImageTk.PhotoImage(file="Cent_bg.png")
       lbl_bg = Label(screen, image=screen.bg)
       lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

       # Frame
       frame = Frame(screen, bg="#5B5B5B")
       frame.place(x=360, y=120, width=330, height=350)

       ''''img1 = Image.open(r"E:\proj_img/user-login-.jpg")
       img1 = img1.resize((100, 100), Image.ANTIALIAS)
       login_screen.photoimage1 = ImageTk.PhotoImage(img1)
       lblimg1 = Label(image=login_screen.photoimage1, borderwidth=0)
       lblimg1.place(x=550, y=75, width=100, height=100)'''

       username = lbl = Label(frame, text="Centre Login", font=("Open sans", 22, "bold"), fg="white", bg="#5B5B5B")
       username.place(x=90, y=25)

       # user text field
       screen.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
       screen.txtuser.place(x=85, y=110, width=225, height=28)

       # password = lb2 = Label(frame, text="Password", font=("times new roman", 20, "bold"), fg="black", bg="skyblue")
       # password.place(x=50, y=215)

       screen.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
       screen.txtpass.place(x=85, y=180, width=225, height=28)

       img2 = Image.open("username_icon.png")
       img2 = img2.resize((40, 40), Image.ANTIALIAS)
       screen.photoimage2 = ImageTk.PhotoImage(img2)
       lblimg1 = Label(image=screen.photoimage2, bg="skyblue", borderwidth=0)
       lblimg1.place(x=390, y=220, width=40, height=40)

       img3 = Image.open("pass_icon.png")
       img3 = img3.resize((40, 40), Image.ANTIALIAS)
       screen.photoimage1 = ImageTk.PhotoImage(img3)
       lblimg1 = Label(image=screen.photoimage1, bg="skyblue", borderwidth=0)
       lblimg1.place(x=390, y=290, width=40, height=40)

       # **Hover
       def changeOnHover(button, colorOnHover, colorOnLeave):
           # background on entering widget
           button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))

           # background color on leving widget
           button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

       # **

       loginbtn = Button(frame, command=login, text="Login", font=("times new roman", 15, "bold"), bd=3,
                         relief=RIDGE, bg="#CFCFCF", activeforeground="black", activebackground="#FFDE59")
       loginbtn.place(x=120, y=240, width=125, height=35)
       changeOnHover(loginbtn, "#6BC145", "#CFCFCF")

       hpbtn = Button(frame, text="Home Page", font=("times new roman", 15, "bold"), borderwidth=0,
                      bg="#CFCFCF", activeforeground="white", activebackground="#FF5757")
       hpbtn.place(x=120, y=290, width=125, height=35)
       changeOnHover(hpbtn, "#5CE1E6", "#CFCFCF")

   def login():
       if screen.txtuser.get() == "" or screen.txtpass.get() == "":
           messagebox.showerror("Error", "All fields required")
       elif screen.txtuser.get() == "abc123" and screen.txtpass.get() == "abc123":
           messagebox.showinfo("Success", "Welcome to Care 19")
       else:
           conn = mysql.connector.connect(host="localhost", user="root", password="hello", database="mini",
                                          auth_plugin='mysql_native_password')
           my_cursor = conn.cursor()
           my_cursor.execute("select * from centre where pass=%s and user=%s",
                             (screen.txtuser.get(), screen.txtpass.get()))

           row = my_cursor.fetchone()
           if row != None:
               messagebox.showerror("Error","Invalid username or password")
           else:
               messagebox.showinfo("Success", "Welcome")

   login_Form()

# centre login ends


# patient login function
'''def main():
   win = Tk()
   app = Login_window(win)
   win.mainloop()'''

'''if __name__ == "__main__":
   root = Tk()
   app = Home_Page(root)
   root.mainloop()'''

# patient login page object
'''if __name__ == "__main__":
   main()'''

