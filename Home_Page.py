import tkinter as tk
from subprocess import run, Popen
from tkinter import ttk
from tkinter import *
from Centre_Login import *
from login import *
from Register_Page import *
from PIL import Image, ImageTk
import os

def Home_page(root):
    root.title("Home Page")
    root.geometry("700x500+250+50")
    tabControl = ttk.Notebook(root)

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

    UR_b = tk.Button(tab1, text="User Register", background="#CFCFCF", activebackground="#6BC145",command=lambda: UR_call(root))
    UR_b.place(x=140, y=420, height=35, width=100)
    changeOnHover(UR_b, "#FFDE59", "#CFCFCF")

    UL_b = tk.Button(tab1, text="User Login", background="#CFCFCF", activebackground="#6BC145",
                     command=lambda: [UL_call(root)])
    UL_b.place(x=315, y=420, height=35, width=100)
    changeOnHover(UL_b, "#FFDE59", "#CFCFCF")

    CL_b = tk.Button(tab1, text="Centre Login", background="#CFCFCF", activebackground="#6BC145",
                     command=lambda: CL_call(root))
    CL_b.place(x=500, y=420, height=35, width=100)
    changeOnHover(CL_b, "#FFDE59", "#CFCFCF")

def UR_call(root):
    root.destroy()
    subprocess.run([sys.executable, 'Register_Page.py'])


def CL_call(root):
    root.destroy()
    subprocess.run([sys.executable, 'Centre_Login.py'])


def UL_call(root):
    root.destroy()
    exec(open('login.py').read())



def call_main():
    root = Tk()
    Home_page(root)
    root.mainloop()


call_main()