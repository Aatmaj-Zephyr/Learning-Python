import tkinter as tk

form=tk.Tk()
form.title("Example of Entry widget")
form.geometry('400x200')

TB1=tk.Entry(form,width = 20)
TB1.pack()
def show():
    button.config(text=TB1.get())
'''
The TB1.get() method returns the string value of the  text inputted into the entry widget. By using the config() method of the button, we can set the text of the button.
'''
button=tk.Button(form,text="", command=show)
button.pack()
form.mainloop()
show()
