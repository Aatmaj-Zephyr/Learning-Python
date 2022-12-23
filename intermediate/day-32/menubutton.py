from tkinter import *
master = Tk()
master.geometry=("300x200")
MB = Menubutton ( master, text="Favorite data analysis" )
MB.menu =  Menu ( MB, tearoff = 0 )
MB["menu"] =  MB.menu

one = IntVar()
two = IntVar()

MB.menu.add_checkbutton ( label="Classification",
                          variable=one )
MB.menu.add_checkbutton ( label="Regression",
                          variable=two )


MB.pack()
mainloop()
