import tkinter
master=tkinter.Tk()
master.geometry('300x300')
master.title("My First Program")
label = tkinter.Label(master, text = "Hello world").place(x = 150, y = 150)
