from tkinter import *
spy=Tk()
spy.geometry("300x200")
spy.title("spyware")
def keypress(event):
    try:
        print(ord(event.char),end=".")
    except: # for blank press
        pass
e1=Entry(spy,show='*')
e1.focus_set()
e1.bind("<Key>",keypress)
# mind the case of 'key'- k must be K
e1.pack()
spy.mainloop()
