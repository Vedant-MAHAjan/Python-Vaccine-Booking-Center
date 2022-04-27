import os
import subprocess
import sys
from tkinter import ttk, messagebox
from tkinter import *
#from PIL import Image, ImageTk
from PIL import Image, ImageTk
import mysql.connector


class Booking_window:
   def __init__(self,root):
      self.root = root
      root.var_centre = StringVar()
      root.var_email = StringVar()

      root.title("Booking Window")
      root.geometry("1350x670+2+2")
      root.bg = ImageTk.PhotoImage(file="Booking.png")
      lb_bg = Label(root, image=root.bg)
      lb_bg.place(x=0, y=0, relwidth=1, relheight=1)

      self.var_Nemail = StringVar()
      self.var_centre = StringVar()
      self.var_name = StringVar()
      self.var_pin = StringVar()

      register_lb1 = Label(root, text="Booking Page", font=("Open sans", 24, "bold"), bg="#545454", fg="white")
      register_lb1.place(x=160, y=130)

      global result
      result = "null"

      pin = Label(root, text="CID :", font=("arial", 16), bg="#545454", fg="white")
      pin.place(x=165, y=225)
      self.pin_entry = ttk.Entry(root, textvariable=self.var_pin, font=("arial", 13))
      self.pin_entry.place(x=240, y=225,height=29,width=210)

      name = Label(root, text="Name :", font=("arial", 16), bg="#545454", fg="white")
      name.place(x=142, y=275)
      self.name_entry = ttk.Entry(root, textvariable=self.var_name, font=("arial", 13))
      self.name_entry.place(x=240, y=275,height=29,width=210)

      email = Label(root, text="Email :", font=("arial", 17), bg="#545454", fg="white")
      email.place(x=141, y=325)
      email_entry = ttk.Entry(root, textvariable=self.var_Nemail, font=("arial", 13))
      email_entry.place(x=240, y=325,height=29,width=210)

      # center choose (combobox
      center = Label(root, text="Center :", font=("arial", 17), bg="#545454", fg="white")
      center.place(x=127, y=375)
      combo_bg = ttk.Combobox(root, textvariable=self.var_centre, width=15, font=("arial", 14), state="readonly")
      combo_bg["values"] = ("Kandivali", "Dahisar", "Vasai")
      combo_bg.place(x=240, y=375,height=29,width=210)

      # test type radiobutton
      test = Label(root, text="Test :", font=("arial", 16), bg="#545454", fg="white")
      s = ttk.Style()  # Creating style element
      s.configure('Wild.TRadiobutton', background="#545454", foreground='white', font=("arial", 13))
      test.place(x=155, y=425)
      var = IntVar()
      r1 = ttk.Radiobutton(root, text="RT-PCR", variable=var, value=1, style='Wild.TRadiobutton')
      r1.place(x=238, y=425)
      r2 = ttk.Radiobutton(root, text="Antigen", variable=var, value=2, style='Wild.TRadiobutton')
      r2.place(x=345, y=425)
      r3 = ttk.Radiobutton(root, text="Rapid RT-PCR", variable=var, value=3, style='Wild.TRadiobutton')
      r3.place(x=440, y=425)

      # home test/center visit radiobutton
      test = Label(root, text="Sample Collection :", font=("arial", 17), bg="#545454", fg="white")
      s = ttk.Style()  # Creating style element
      s.configure('Wild.TRadiobutton', background="#545454", foreground='white', font=("arial", 13))
      test.place(x=17, y=475)
      var1 = IntVar()
      r1 = ttk.Radiobutton(root, text="Home", variable=var1, value=1, style='Wild.TRadiobutton')
      r1.place(x=238, y=475)
      r2 = ttk.Radiobutton(root, text="Center Visit", variable=var1, value=2, style='Wild.TRadiobutton')
      r2.place(x=320, y=475)

      # 3 buttons
      bt1 = Button(root, text="Back", background="#CFCFCF", activebackground="#6BC145", font=("Arial", 13),
                   command=lambda: UL_call(root))
      bt1.place(x=120, y=550, height=42, width=100)
      changeOnHover(bt1, "#FF5757", "#CFCFCF")

      bt2 = Button(root, text="Book Test", command=self.add_data, background="#CFCFCF",
                   activebackground="#6BC145", font=("Arial", 13))
      bt2.place(x=260, y=550, height=42, width=100)
      changeOnHover(bt2, "#6BC145", "#CFCFCF")

   def add_data(self):
      if self.var_centre.get() == "":
         messagebox.showerror("Error", "All fields required")
      else:
         conn = mysql.connector.connect(host="localhost", user="root", password="hello", database="mini",
                                        auth_plugin='mysql_native_password')
         my_cursor = conn.cursor()

         my_cursor.execute("insert into book_table values(%s,%s,%s,%s,null)",
                     (self.var_pin.get(),self.var_name.get(),self.var_Nemail.get(),self.var_centre.get()))
         #print(my_cursor)
         conn.commit()
         conn.close()
#         print()
         messagebox.showinfo("Success", "Registered Successfully")


# Hover
def changeOnHover(button, colorOnHover, colorOnLeave):
   # background on entering widget
   button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))

   # background color on leving widget
   button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))


def UL_call(root):
   root.destroy()
   #subprocess('python login.py')
   subprocess.run([sys.executable, 'login.py'])

if __name__ == "__main__":
   root = Tk()
   app = Booking_window(root)
   root.mainloop()