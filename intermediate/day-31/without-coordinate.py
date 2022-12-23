from tkinter import *
master=Tk()
master.geometry("300x200")

Lbl1=Label(master,text="Principle")
Lbl2=Label(master,text="Discount")
Lbl3=Label(master,text="Total. ",font="20px")
spinbox=Spinbox(master,from_=10, to=100)
slider=Scale(master,from_=0, to=100, tickinterval=20, length= 150, orient="horizontal")
def display():
    a=int(spinbox.get())-int(spinbox.get())*int(slider.get())/100
    Lbl3.config(text=str(a)+"$")
button=Button(master,text="Calculate",command=display)

spinbox.pack()
Lbl1.pack()
slider.pack()
Lbl2.pack()
button.pack()
Lbl3.pack()

mainloop()
