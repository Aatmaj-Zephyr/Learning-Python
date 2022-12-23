from tkinter import *
frame=Tk()
frame.geometry("200x200")
slider=Scale(frame,from_=0, to=10, orient="horizontal")
slider.set(2)
slider.pack()
def reset():
    slider.set(2)
resetbutton=Button(frame,text="reset",command=reset)
resetbutton.pack()
mainloop()
