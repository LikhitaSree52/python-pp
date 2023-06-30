from tkinter import *

win=Tk() 
win.title('Welcome') 


can=Canvas(win, width=500, height=500) 
oval=can.create_oval(250,250,250,250,fill='green')  
can.pack()

win.mainloop() 
