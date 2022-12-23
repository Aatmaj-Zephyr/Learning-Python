import tkinter as tk

form=tk.Tk()
form.title("Example of Entry widget")
form.geometry('400x200')
a=tk.IntVar()
def count():
    a.set(a.get()+1)
    button.config(text=str(a.get()))#don't forget the str()

button=tk.Button(form,text="Press Me",command=count)
button.pack()
form.mainloop()
show()
