from tkinter import messagebox
from tkinter import *
master = Tk()
master.geometry("100x100")
def showmessage():
   messagebox.showwarning("Wait!","Something is missing")
button=Button(master,text="Show message",command=showmessage)
button.pack()
master.mainloop()
