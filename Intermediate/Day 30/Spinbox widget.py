from tkinter import *
frame=Tk()
frame.geometry("200x200")
spinbox=Spinbox(frame,from_=0, to=10)

spinbox.pack()
def show():
    showbutton.config(text=spinbox.get())
showbutton=Button(frame,text="show",command=show)
showbutton.pack()
mainloop()
