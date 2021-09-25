# [Learning Python- Intermediate course: Day 32, The Menubutton Widget](https://dev.to/aatmaj/learning-python-intermediate-course-day-32-the-menubutton-widget-4l0j)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-32-the-menubutton-widget-4l0j)

In this part let us learn about the menubutton widget.
---
____
## Menubutton widget
The menubutton widget is a drop down type of widget. It looks similar to the listbox widget. The menubutton widget is dropped down once the menubutton button is clicked.
____
Here is a sample program.

```python
from tkinter import *
master = Tk()
master.geometry=("300x200")
MB = Menubutton ( master, text="Favorite data analysis" )
MB.menu =  Menu ( MB, tearoff = 0 )
MB["menu"] =  MB.menu

one = IntVar()
two = IntVar()

MB.menu.add_checkbutton ( label="Classification",
                          variable=one )
MB.menu.add_checkbutton ( label="Regression",
                          variable=two )


MB.pack()
mainloop()

```

- `MB = Menubutton ( master, text="" )` Create a menubutton with text and the window frame parameters.

- `MB.menu =  Menu ( MB, tearoff = 0 )` `MB["menu"] =  MB.menu` Create a menu object and configure it with the menubutton.

- `MB.menu.add_checkbutton ( label="Classification",
                          variable=one )` Add a button to the menubutton and control it using the `Intvar()` classes. This is very similar to how we operated on checkboxes and radiobuttons. In case you have missed it, you can check it out [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-23-intvar-and-radio-buttons-164k)


![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rsihy1p6d9sohvnfxztq.png)
 ![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uodtuaresrhmirfrz44p.png)
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2329jh7qvwvls1onf6nc.png)
 
 ![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/yu0wly4kfx4tnhk2sjbg.png)
 ![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kcjiw65bs2t6bmqodg2q.png)

### The tearoff parameter. The `tearoff` parameter is present if we want to remove the window and create a sub-window for the parameters. For example, removing the `tearoff` parameter to the default settings will show a result like this-
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sgslkb1rpcjz231l4sur.png)
 
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8vmg6foz4mp6mddggpzf.png)
 

But if we click on the horizontal dotted line, the dropdown tears apart into a different window

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ymc00hm4m1aaubtunc0z.png)
 
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/77zazani5timfbjl5x2u.png)
 
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r4w4w3n7qdqop8pgn3ft.png)
We can create multiple windows in such manner.
 ![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/arfuzy28zjoqvsq49kea.png)
 

### Summary of the week

- [Learning Python- Intermediate course: Day 29, Sliders in Tkinter](https://dev.to/aatmaj/learning-python-intermediate-course-day-29-sliders-in-tkinter-5a6d) We covered sliders in Tkinter. Slider is a type of widget which lets the user choose variable values in a graphical and interactive manner. We saw how to set various parameters like the interval length, length and orientation of the slider. We saw the getter and setter methods of the widget.

- [Learning Python- Intermediate course: Day 30, Spinbox and Labelbox](https://dev.to/aatmaj/learning-python-intermediate-course-day-30-spinbox-and-labelbox-1b35)- We checked out the spinbox and the labelbox widgets. The spinbox widget is a widget which is used to get input from the user navigated through up and down keys. The listbox is a menu type widget which helps the users select from a list of items. We also saw the various types of parameters of the listbox widget, for example the types of selections and length of the listbox. We saw the getter and setter methods of the widget. The type of selection of the listboxes include `BROWSE` `SINGLE` `MULTIPLE` and `EXTENDED `

- [Learning Python- Intermediate course: Day 31, Coordinate positions](https://dev.to/aatmaj/learning-python-intermediate-course-day-31-coordinate-positions-4eah) In this part, we made a sample practice program to calculate the discount prices. In this, we used both the spinbox and the slider widgets. In order to place the widgets around in the desired manner, wee used coordinate placing using the `.place()` method. Using this method, we placed the widgets in proper x and y coordinates.

_____
So friends that was all for this week. Hope you all are having fun 👍
