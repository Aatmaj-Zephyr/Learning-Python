# [Learning Python- Intermediate course: Day 33, The Menu Widget](https://dev.to/aatmaj/learning-python-intermediate-course-day-33-the-menu-widget-5g5l)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-33-the-menu-widget-5g5l)

Today we will cover menu widget in Tkinter
---
____
In the previous part, we learnt to use menubutton. Today we will learn a very similar widget called as the menu widget.

### The menu widget
The menu widget is a type of widget which lets the users choose actions from a drop down. We see menus everywhere in any GUI application. For example, in the Python IDLE itself there is a men widget.

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/62253dleme6v337z8zzu.png)
 
 The menu widget is responsible for many important actions. Save, save as, open a file, quitting a program, undo, redo, etc are a few actions to name.

> The top-level menus are the one which is displayed just under the title bar of the parent window. 

### Making a menu widget
We can make a menu widget by using the syntax `menubar = Menu(master)` 
This creates an instance of the menu-widget. Afert that, we need ot create an instance of a menubar button by adding parameters to the `menu()` constructor. That is, `file = Menu(menubar, tearoff=0) `. This creates a button named file (we add txt later) on the top of the screen. We do that for every button we want to place on the top menu. Example here we add two buttons, file and edit.
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qqd3j6cafxrg3f0kc4nb.png)
 

 Now we need to add add various commands to it by using the `add_comand()` method. These are displayed in the dropdown. Example `file.add_command(label="New")  ` We can also use the command `file.add_separator()` to add a horizontal line for separation 

After we are done adding the commands, to the dropdown, we can use the command `menubar.add_cascade(label="File", menu=file)` to set the txt of the button and place it in the main menu.

The entire program is as follows--


____

```python
from tkinter import *
master = Tk()  
menubar = Menu(master)

file = Menu(menubar, tearoff=0)  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as")
file.add_separator()
file.add_command(label="Exit")  
menubar.add_cascade(label="File", menu=file)
                 
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
edit.add_separator()  
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")  
menubar.add_cascade(label="Edit", menu=edit)

master.config(menu=menubar)  
master.mainloop()  

```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/msoyhg8z1r50uqlzy0hd.png)
 

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/eb6lx9osbe6csxks5izm.png)

> In the above program, clicking on the buttons will not run any actions, as we have not placed any command on clicking.

____
So friends that was all for today, Stay tuned and follow me for updates.
 
