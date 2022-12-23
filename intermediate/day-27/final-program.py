import tkinter as tk # import the Tkinter module

form=tk.Tk() # create the blank window.
form.title("password manager") # set the title as password manager
form.geometry('400x200') # set the default geometry of the window.

TB1=tk.Entry(form, width = 20) 
# make an entry widget with 20 spaces for the username

TB2=tk.Entry(form,show="*", width = 20)
def keypress(event):
    try:
        print(ord(event.char),end=".")
    except: # for blank press
        pass
TB2.bind("<Key>",keypress)
# entry widget for password and hide the keys whenever pressed.

# TB1 is for username, TB2 is for password
TB1.pack()
TB2.pack()
# pack the widgets into 'form'

label=tk.Label(form,text="")
# make a label to display the username

def show(): #function to be executed once the button is pressed.
    a=TB1.get() # get username
    b=TB2.get() # get password
    if(a!="" and b!=""):
     label.config(text="Welcome "+a+" to python GUI",fg="Green") # display the label
     storepassword(a,b) # store password and username
    else:
     label.config(text="Please enter a valid username and password.",fg="Red")  # blank screens

def storepassword(username, password):
    #//Some mechanism to store password//
    pass #stubbed

button=tk.Button(form,text="Sign Up", command=show) # setup the button
button.pack()
label.pack()
form.mainloop()
show()
