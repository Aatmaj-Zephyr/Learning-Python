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

# Set geometry
spinbox.place(x=100, y=0)
Lbl1.place(x=0,y=0)
slider.place(x=100, y=50)
Lbl2.place(x=0,y=70)
button.place(x=150,y=130)
Lbl3.place(x=150,y=170)

mainloop()
