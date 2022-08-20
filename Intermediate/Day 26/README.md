# [Learning Python- Intermediate course: Day 26, Password Manager-Tkinter](https://dev.to/aatmaj/learning-python-intermediate-course-day-26-password-manager-tkinter-17p9)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-26-password-manager-tkinter-17p9)

## Let us build a login application which gets the passwords and usernames from users.

---

#### Today's application specs are as follows

1. There are four widgets- two Entry (single line textboxes), one button, one label in the program.
2. The user enters username in the first textbox. Password in the second textbox. But the password is encrypted (not shown)
3. After user hits the sign up button, the username is displayed on the label and the password is stored.
   _We will not store the password now, just make a dummy password entry function stub. The password can be stored in files in encrypted format or by other methods once we cover file handling in Python. Till that time, assume that the `storepassword()` function stores the passwords and username automatically_

---

### Encrypting the entry widget.

We don't want others to see our passwords while we type them right? This can be achieved using the `show="*"` attribute.

`TB1=tk.Entry(form,width = 20,show="*")`

```python
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

```

Let us now revisit yesterday's program and hide the entry widget.

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u7fnlzgtlvi6j4u68wlm.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3jro1sgx61nxlamrp3eb.png)

---

### Building the login screen.

We already have got the specifications of the program, so now let us start building it. Here is the code for the program, commented for explaination. Be sure to give it a try first before seeing the solution.

```python
import tkinter as tk # import the Tkinter module

form=tk.Tk() # create the blank window.
form.title("password manager") # set the title as password manager
form.geometry('400x200') # set the default geometry of the window.

TB1=tk.Entry(form, width = 20)
# make an entry widget with 20 spaces for the username

TB2=tk.Entry(form,show="*", width = 20)
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
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bj1exu1iyw0euab3zccb.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zqkz4sr1yi5xj5x85l4z.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/y9fp3rzsh17lniyahevu.png)

---

**Homework** Run the above application _(without seeing)_ debug and test it. Store the application in a file passwordmanager.pyw. and send me a pic on the comments on [dev.to](https://dev.to/aatmaj/learning-python-intermediate-course-day-26-password-manager-tkinter-17p9) or forking this file.

---

Well this password manager is very secure....But in the next part we will see a mechanism to steal the passwords by a spyware😈
So stay tuned for updates by following me.
