from tkinter import *
frame = Tk()
frame.geometry("200x200")
items=("Python","R","Julia","MATLAB","Mathematica","Haskell")
Lb = Listbox(frame,selectmode=EXTENDED)
for i in range(0,len(items)):
    Lb.insert(i,items[i])

Lb.pack()

mainloop()
frame.mainloop()
