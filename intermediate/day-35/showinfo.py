from tkinter import messagebox
from tkinter import *
master = Tk()
master.geometry("100x100")
def showmessage():
   messagebox.showinfo("Say hello","Hello programmers")
button=Button(master,text="Show message",command=showmessage)
button.pack()
master.mainloop()
