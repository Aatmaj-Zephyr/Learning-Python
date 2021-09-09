from tkinter import *

window=Tk()
#create a window frame called master
window.title("Checkboxes")
window.geometry("250x100")

label=Label(window,text="text")
#create a label with text 'empty' and put it in the window frame

def ChangeLabel():
    if(bold.get() == 1 and italics.get() == 0):
        label.config(text='bold',font=('Helvetica', 18, 'bold'))
    elif(bold.get() ==0 and italics.get() == 1):
        label.config(text='italics',font=('Helvetica', 18, 'italic'))
    elif(bold.get() ==1 and italics.get() == 1):
        label.config(text='bold and italics',font=('Helvetica', 18, 'bold italic'))
    else:
        label.config(text='text',font=('Helvetica', 18, ''))

bold= BooleanVar()
italics= BooleanVar()
Boldcheckbox= Checkbutton(window,text="Bold", variable= bold, onvalue=1,offvalue=0,command=ChangeLabel)
Italicscheckbox= Checkbutton(window,text="Italics", variable= italics, onvalue=1,offvalue=0,command=ChangeLabel)

label.pack()
Boldcheckbox.pack()
Italicscheckbox.pack()
#pack in the order of appearance.

# The mainloop() attributes must be at the end of the program
window.mainloop()
