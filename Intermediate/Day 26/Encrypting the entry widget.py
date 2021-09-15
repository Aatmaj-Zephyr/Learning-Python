import tkinter as tk

form=tk.Tk()
form.title("Example of Entry widget")
form.geometry('400x200')

TB1=tk.Entry(form,width = 20,show="*")
TB1.pack()
def show():
    button.config(text=TB1.get())
button=tk.Button(form,text="", command=show)
button.pack()
form.mainloop()
show()
