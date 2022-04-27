import subprocess
import sys
from atexit import register
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os



class Login_window:

   def __init__(self, root):
       self.root = root
       self.root.title("User Login")
       self.root.geometry("700x500")

       self.bg = ImageTk.PhotoImage(file="User_login.png")
       lbl_bg = Label(self.root, image=self.bg)
       lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        #Frame
       frame = Frame(self.root, bg="#5B5B5B")
       frame.place(x=360, y=120, width=330, height=350)

       username = lbl = Label(frame, text="User Login", font=("Open sans", 22, "bold"), fg="white", bg="#5B5B5B")
       username.place(x=105, y=25)

       #user text field
       #global txtuser
       self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
       self.txtuser.place(x=85, y=110, width=225,height=28)

       #password = lb2 = Label(frame, text="Password", font=("times new roman", 20, "bold"), fg="black", bg="skyblue")
       #password.place(x=50, y=215)

       #global txtpass
       self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"),show="*")
       self.txtpass.place(x=85, y=180, width=225,height=28)

       img2 = Image.open("username_icon.png")
       img2 = img2.resize((40, 40), Image.ANTIALIAS)
       self.photoimage2 = ImageTk.PhotoImage(img2)
       lblimg1 = Label(image=self.photoimage2, bg="skyblue", borderwidth=0)
       lblimg1.place(x=390, y=220, width=40, height=40)

       img3 = Image.open("pass_icon.png")
       img3 = img3.resize((40, 40), Image.ANTIALIAS)
       self.photoimage1 = ImageTk.PhotoImage(img3)
       lblimg1 = Label(image=self.photoimage1, bg="skyblue", borderwidth=0)
       lblimg1.place(x=390, y=290, width=40, height=40)

       #**Hover
       def changeOnHover(button, colorOnHover, colorOnLeave):
           # background on entering widget
           button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))

           # background color on leving widget
           button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

       #**

       loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3,
                         relief=RIDGE,bg="#CFCFCF", activeforeground="black", activebackground="#FFDE59")
       loginbtn.place(x=120, y=240, width=125, height=35)
       changeOnHover(loginbtn, "#6BC145", "#CFCFCF")

       hpbtn = Button(frame, text="Home Page", font=("times new roman", 15, "bold"), borderwidth=0,
                            bg="#CFCFCF", activeforeground="white", activebackground="#FF5757",command=lambda :HPcall(root))
       hpbtn.place(x=120, y=290,  width=125, height=35)
       changeOnHover(hpbtn, "#5CE1E6", "#CFCFCF")

   def login(self):

       if self.txtuser.get() == "" or self.txtpass.get() == "":
           messagebox.showerror("Error", "All fields required")

       elif len(self.txtuser.get()) < 3 or len(self.txtpass.get()) < 3:
           messagebox.showerror("Error", "Enter atleast 3 characters.")

       elif self.txtuser.get().isdigit() == True:
           messagebox.showerror("Error", "Only numbers are not allowed.")

       if self.txtuser.get() == "" or self.txtpass.get() == "":
           return messagebox.showerror("Error", "All fields required")

       else:
           conn = mysql.connector.connect(host="localhost", user="root", password="hello", database="mini",
                                           auth_plugin='mysql_native_password')
           my_cursor = conn.cursor()
           my_cursor.execute("select * from new_table where fname=%s and pass=%s",
                             (self.txtuser.get(), self.txtpass.get()))

           row = my_cursor.fetchone()
           if row != None:
               messagebox.showerror("Error", "Invalid username or password")
               #print(row)
           else:
               messagebox.showinfo("Success", "Welcome to Care 19")
               self.root.destroy()
               subprocess.run([sys.executable, 'book.py'])




def HPcall(root):
    root.destroy()
    subprocess.run([sys.executable, 'Home_Page.py'])


if __name__ == "__main__":
   root = Tk()
   app = Login_window(root)
   root.mainloop()






