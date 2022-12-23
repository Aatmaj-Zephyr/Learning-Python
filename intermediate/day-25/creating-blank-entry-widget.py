import tkinter as tk

form=tk.Tk()
form.title("Example of Entry widget")
form.geometry('400x200')


TB1=tk.Entry(form,width = 20)
TB1.pack()

form.mainloop()
show()
