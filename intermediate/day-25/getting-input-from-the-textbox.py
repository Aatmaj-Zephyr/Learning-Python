import tkinter as tk

form=tk.Tk()
form.title("Example of Entry widget")
form.geometry('400x200')

TB1=tk.Text(form,width = 7,height=5)
TB1.pack()
def show():
    button.config(text=TB1.get(1.0, "end-1c"))
'''
get(start, [end])
where,
start is starting index of required text in TextBox,
end is ending index of required text in TextBox
'''
button=tk.Button(form,text="", command=show)
button.pack()
form.mainloop()
show()
