# [Learning Python- Intermediate course: Day 34, Toplevel, Panedwindow and Message widgets](https://dev.to/aatmaj/learning-python-intermediate-course-day-34-toplevel-panedwindow-and-message-widgets-44l6)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-34-toplevel-panedwindow-and-message-widgets-44l6)

Today we will cover a brief about the Top-level, paned-window and message widgets.
---
____
Till now we have covered majority of the widgets. Today's agenda is  to have a quick look at three more widgets without going too much into the depth. I will just provide a short explaination and the code for creating the widget. So let's get started. 

### Top level widget

The Toplevel widget is used to create popup like windows. These toplevel windows are directly managed by the window manager. 

> The toplevel widget is used to represent some extra information, pop-up, or the group of widgets on the new window. The toplevel windows have the title bars, borders, and other window decorations.

```python
from tkinter import *  
  
master= Tk()  
  
master.geometry("200x200")  
  
def open():  
    top = Toplevel(root)  
    top.mainloop()  
  
btn = Button(master, text = "pop", command = open)  
  
btn.place(x=75,y=50)  
  
master.mainloop()  
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z174cjha7ljqk3gp5x5k.png)
 
On several clicks....

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/saqjr54bufeiy2d3v2en.png)
 

### Panedwindow


The Paned Window widget acts like a Container widget which contains one or more child widgets (panes) arranged horizontally or vertically. The child panes can be resized by the user, by moving the separator lines known as sashes by using the mouse.

Each pane contains only one widget. The Paned Window is used to implement the different layouts in the python applications.

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uf0joygogfha28g2tqfk.png)
```python
from tkinter import *  
master=Tk()
  
win = PanedWindow(orient='vertical')
lbl=Label(text="paned window")
win.add(lbl)
win.pack()
  
  
mainloop() 
``` 

____
### Message widget 
The message widget is similar to the label widget. It has a few advantages over the label widget, like it can automatically wrap the text, maintaining a given width or aspect ratio

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/br01v3c8gtwge4gj65e6.png)
 
```python
from tkinter import *

master = Tk()
var = StringVar()
msg = Message( master, textvariable=var )

var.set("Bye!")
msg.pack()
master.mainloop()

```
In order to set the text contents of the message widget, we need to create a `stringvar()` object to store the message and then out it in the message widget.



____
So friends that was all for this part. Message-box widget coming soon...... 

Follow me for updates..........
