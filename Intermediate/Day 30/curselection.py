from tkinter import *
frame = Tk()
frame.geometry("200x200")

Lb = Listbox(frame)
Lb.insert(1, "Python")
Lb.insert(2, "R")
Lb.insert(3, "Julia")
Lb.insert(4, "MATLAB")
Lb.insert(5, "Mathematica")
Lb.insert(6, "Haskell")

Lb.pack()
def show():
    showbutton.config(text=Lb.curselection())
showbutton=Button(frame,text="show",command=show)
showbutton.pack()
mainloop()
frame.mainloop()
