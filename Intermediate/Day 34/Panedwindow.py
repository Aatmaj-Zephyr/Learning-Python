from tkinter import *  
master=Tk()
  
win = PanedWindow(orient='vertical')
lbl=Label(text="paned window")
win.add(lbl)
win.pack()
  
mainloop() 
