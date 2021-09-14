import tkinter as tk

form=tk.Tk()
form.title("Example of textbox widget")
form.geometry('400x200')

TB1=tk.Text(form,width = 5,height = 5)
TB1.pack()

form.mainloop()
show()
