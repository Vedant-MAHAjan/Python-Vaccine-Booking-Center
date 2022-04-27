from tkinter import *
def fun():
    def login():
        uname=username.get()
        pwd=password.get()
        if uname=='' or pwd=='':
            message.set("Please fill the empty fields.")
        else:
          if uname=="abcd@gmail.com" and pwd=="abc123":
           message.set("Login success.")
          else:
           message.set("Wrong username or password.")

    def Loginform():
        global login_screen
        login_screen = Tk()
        login_screen.configure(bg="grey")
        login_screen.title("Login Form")
        login_screen.geometry("500x300")
        global  message;
        global username
        global password
        username = StringVar()
        password = StringVar()
        message=StringVar()
        Label(login_screen,height="2",width="300", text="Please enter details below", bg="orange",fg="white").pack()
        Label(login_screen, text="Username * ").place(x=160,y=70)
        Entry(login_screen, textvariable=username).place(x=250,y=72)
        Label(login_screen, text="Password * ").place(x=160,y=140)
        Entry(login_screen, textvariable=password ,show="*").place(x=250,y=140)
        Label(login_screen, text="",textvariable=message,bg="grey").place(x=250,y=170)
        Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=230,y=220)
        login_screen.mainloop()
    Loginform()
