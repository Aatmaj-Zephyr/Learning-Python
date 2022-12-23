from tkinter import *
frame = Tk()
frame.geometry("200x200")
items=("Python","R","Julia","MATLAB","Mathematica","Haskell")
Lb = Listbox(frame)
for i in range(0,len(items)):
    Lb.insert(i,items[i])

Lb.pack()
def show():
    showbutton.config(text=items[Lb.curselection()[0]])
showbutton=Button(frame,text="show",command=show)
showbutton.pack()
mainloop()
frame.mainloop()
