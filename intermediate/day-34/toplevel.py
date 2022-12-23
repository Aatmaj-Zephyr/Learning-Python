from tkinter import *  
  
master= Tk()  
  
master.geometry("200x200")  
  
def open():  
    top = Toplevel(root)  
    top.mainloop()  
  
btn = Button(master, text = "pop", command = open)  
  
btn.place(x=75,y=50)  
  
master.mainloop()  
