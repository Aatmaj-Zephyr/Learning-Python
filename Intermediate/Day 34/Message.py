from tkinter import *

master = Tk()
var = StringVar()
msg = Message( master, textvariable=var )

var.set("Bye!")
msg.pack()
master.mainloop()
