from tkinter import messagebox
from tkinter import *
master = Tk()
master.geometry("100x100")
def showmessage():
   a=messagebox.askyesno("stop!","are you sure?")
   #returns true or false
   button.config(text=a)

button=Button(master,text="Show message",command=showmessage)
button.pack()
master.mainloop()
