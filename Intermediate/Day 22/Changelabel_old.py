from tkinter import *

window=Tk()
#create a window frame called master
window.title("Checkboxes")
window.geometry("250x100")

label=Label(window,text="text")
#create a label with text 'empty' and put it in the window frame

def ChangeLabel(bold,italics):
    if(bold == True and italics == False):
        label.config(text='bold',font=('Helvetica', 18, 'bold'))
    elif(bold ==False and italics == True):
        label.config(text='italics',font=('Helvetica', 18, 'italic'))
    elif(bold ==True and italics == True):
        label.config(text='bold and italics',font=('Helvetica', 18, 'bold italic'))
    else:
        label.config(text='text',font=('Helvetica', 18, ''))

bold= False
italics= True
ChangeLabel(bold,italics)


label.pack()
# The pack() and mainloop() attributes must be at the end of the program
window.mainloop()
