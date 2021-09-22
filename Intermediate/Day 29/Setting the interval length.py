from tkinter import *
frame=Tk()
frame.geometry("200x200")
slider=Scale(frame,from_=0, to=10, tickinterval=1, orient="horizontal")
slider.set(2)
slider.pack()
def reset():
    resetbutton.config(text=slider.get())
resetbutton=Button(frame,text="show",command=reset)
resetbutton.pack()
mainloop()
