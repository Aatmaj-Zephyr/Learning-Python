from tkinter import messagebox
from tkinter import *
master = Tk()
master.geometry("100x100")
def showmessage():
   messagebox.askyesno("stop!","are you sure?")
button=Button(master,text="Show message",command=showmessage)
button.pack()
master.mainloop()
