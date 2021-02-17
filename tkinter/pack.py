# !/usr/bin/python3  
from tkinter import *  
  
parent = Tk()  
  
redbutton = Button(parent, text = "Red", fg = "red")  
redbutton.pack( side = LEFT)  
  
greenbutton = Button(parent, text = "Black", fg = "black")  
greenbutton.pack( side = RIGHT )  
  
bluebutton = Button(parent, text = "Blue", fg = "blue")  
bluebutton.pack( side = TOP )  
  
blackbutton = Button(parent, text = "Green", fg = "green")  
blackbutton.pack( side = BOTTOM)  
  
parent.mainloop()  
