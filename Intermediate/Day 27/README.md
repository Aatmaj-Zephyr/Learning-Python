# [Learning Python- Intermediate course: Day 27, Entry keypress event](https://dev.to/aatmaj/learning-python-intermediate-course-day-27-entry-keypress-event-5d15)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-27-entry-keypress-event-5d15)

Let us study keypress event in Tkinter entry widget
---
____
In the last part we had made a dummy login program (password manager). But the thing was the password was hidden. The password data can only be accessed by the `storepassword()` function. But today how about making a secret trapdoor available for hackers to steal the passwords😈

### Keypress event
We can achieve this by writing a piece of code into the main program which scans whatever we write into the password entry widget and prints it in the command prompt. This can be done using the keypress event. `e1.bind("<Key>",keypress)` Whenever any key is pressed, then the function 'keypress' is executed.

Here is the complete code
```python
from tkinter import *
spy=Tk()
spy.geometry("300x200")
spy.title("spyware")
def keypress(event):
    try:
        print(ord(event.char),end=".")
    except: # for blank press
        pass
e1=Entry(spy,show='*')
e1.focus_set()
e1.bind("<Key>",keypress)
# mind the case of 'key'- k must be K
e1.pack()
spy.mainloop()

```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fhouxyr5pyx8kiwuy3w3.png)
 
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/a6vou6e6u6qzy2g4ysp4.png)


So what is happening? Well, the actual action is taking place in the shell window. 

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9183o8sfeit3l5h2iqzb.png)
 
Let me explain what the keypress function does. Whenever any key is pressed, the keypress function is executed. This function first extracts out which key is pressed. Then, it converts the key into an ASCII value and prints it in the command shell using a dot for separation. This way, even characters like backspace and enter key can be detected. Parsing this string to get the password is a piece of cake for the hacker😈

> The code is wrapped in try-except to prevent blank key presses, which results in errors like ```
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\aatma\AppData\Local\Programs\Python\Python310\lib\tkinter\__init__.py", line 1884, in __call__
    return self.func(*args)
  File "C:/Users/aatma/AppData/Local/Programs/Python/Python310/spy.py", line 6, in keypress
    print(ord(event.char),end=".")
TypeError: ord() expected a character, but string of length 0 found
```

___
Let us now couple the code with our password manager and see the results.
```python
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

```
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ejhmpyrynk9nunsmb62u.png)
 

____
So friends that was all for this part. Stay tuned for updates.....
