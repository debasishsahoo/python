# !/usr/bin/python3  
from tkinter import *  
  
top = Tk()  
  
top.geometry("400x250")  
  
name = Label(top, text = "Name").place(x = 30,y = 50)  
  
email = Label(top, text = "Email").place(x = 30, y = 90)  
  
password = Label(top, text = "Password").place(x = 30, y = 130)  
  
e1 = Entry(top).place(x = 80, y = 50)  
  
  
e2 = Entry(top).place(x = 80, y = 90)  
  
  
e3 = Entry(top).place(x = 95, y = 130)  
  
top.mainloop()  
