# [Learning Python- Intermediate course: Day 30, Spinbox and Labelbox](https://dev.to/aatmaj/learning-python-intermediate-course-day-30-spinbox-and-labelbox-1b35)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-30-spinbox-and-labelbox-1b35)

In this part let us see how to use the spinbox and listbox widgets widget.
---
____
## Spin box widget.
The spinbox widget is a type of widget which lets the users choose values in an easy way. The user can navigate through the values using the up and down arrows. You can read more about it [here](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/spinbox.html)

### Making the spinbox widget
The spinbox widget is very similar to the slider widget we learnt in the last part. `v` all we need to do is replace slider by spinbox


```python
from tkinter import *
frame=Tk()
frame.geometry("200x200")
spinbox=Spinbox(frame,from_=0, to=10)

spinbox.pack()
def show():
    showbutton.config(text=spinbox.get())
showbutton=Button(frame,text="show",command=show)
showbutton.pack()
mainloop()
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qc3et3mzybli3ky0rcll.png)
 
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7efky3z3yzxlcfxoeskf.png)
 
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/la37pd672vh4yb20a9ga.png)

Here we get the value from the spinbox in the same manner as we did for slider widget, that is, by using the `get()` method.
 
## Listbox widget
The listbox widget also allows the users to choose values from a given set of string or numerical values. These value sets are determined by the program. 
> The Listbox widget is used to display a list of items from which a user can select a number of items.

### Making a listbox widget
`Lb = Listbox(frame)` creates a listbox widget. We can add values to the widget using the `insert()` method. 
Here is an example which creates a Listbox

```python
from tkinter import *
frame = Tk()
frame.geometry("200x200")

Lb = Listbox(frame)
Lb.insert(1, "Python")
Lb.insert(2, "R")
Lb.insert(3, "Julia")
Lb.insert(4, "MATLAB")
Lb.insert(5, "Mathematica")
Lb.insert(6, "Haskell")

Lb.pack()
frame.mainloop()
```

### Getting the value from the listbox. 
We can get the value using the `curselection()` method. The curselection returns the position of the selected item.

```python
from tkinter import *
frame = Tk()
frame.geometry("200x200")

Lb = Listbox(frame)
Lb.insert(1, "Python")
Lb.insert(2, "R")
Lb.insert(3, "Julia")
Lb.insert(4, "MATLAB")
Lb.insert(5, "Mathematica")
Lb.insert(6, "Haskell")

Lb.pack()
def show():
    showbutton.config(text=Lb.curselection())
showbutton=Button(frame,text="show",command=show)
showbutton.pack()
mainloop()
frame.mainloop()
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7uyohpnk8ltlaqk4lctm.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7rwdbysjk1x979bh6cs1.png)
 
In order to get the value, we can use listbox method `get()` to return the tuple of values and index the position.`showbutton.config(text=Lb.get(Lb.curselection()))`
But instead it will be more flexible if we make a tuple of those values themselves and feed them into the program. moreover using a for loop to feed in values enhances flexibility and extensibility.

```python
from tkinter import *
frame = Tk()
frame.geometry("200x200")
items=("Python","R","Julia","MATLAB","Mathematica","Haskell")
Lb = Listbox(frame)
for i in range(0,len(items)):
    Lb.insert(i,items[i])

Lb.pack()
def show():
    showbutton.config(text=items[Lb.curselection()[0]])
showbutton=Button(frame,text="show",command=show)
showbutton.pack()
mainloop()
frame.mainloop()
```
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3jfujp1a322mtapuvu4e.png)
 
Exercise-
1) Should `item` be a tuple or a list??
2) What will happen if we remove `[0]` in `items[Lb.curselection()[0]]`?
3) Use `Lb.get(Lb.curselection())` and rewrite the entire program
4) The above program, lot of lines are wasted. use the `height` attribute to adjust the number of lines.
5) Does the height attribute take in the number of lines or pixel space? Try to find out using trial and error methods.
6) When you set the height, did you feel the usefulness of flexibility initializing a tuple and setting the values?

Answer in the comments below. Answers will be found in the [Learning Python Repository](https://github.com/Aatmaj-Zephyr/Learning-Python)


### Types of selections
In the listbox object, there is a attribute called as `selectmode`. By using this attribute, we can set how we want to select the items.
> Selectmode determines how many items can be selected, and how mouse drags affect the selection −
- BROWSE − Normally, you can only select one line out of a listbox. If you click on an item and then drag to a different line, the selection will follow the mouse. This is the default.
- SINGLE − You can only select one line, and you can't drag the mouse. Wherever you click button 1, that line is selected.
- MULTIPLE − You can select any number of lines at once. Clicking on any line toggles whether or not it is selected.
- EXTENDED − You can select any adjacent group of lines at once by clicking on the first line and dragging to the last line.

```PYTHON
from tkinter import *
frame = Tk()
frame.geometry("200x200")
items=("Python","R","Julia","MATLAB","Mathematica","Haskell")
Lb = Listbox(frame,selectmode=MULTIPLE)
for i in range(0,len(items)):
    Lb.insert(i,items[i])

Lb.pack()

mainloop()
frame.mainloop()

```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ibbq5hroe9nqa220u1c0.png)

```python
from tkinter import *
frame = Tk()
frame.geometry("200x200")
items=("Python","R","Julia","MATLAB","Mathematica","Haskell")
Lb = Listbox(frame,selectmode=EXTENDED)
for i in range(0,len(items)):
    Lb.insert(i,items[i])

Lb.pack()

mainloop()
frame.mainloop()
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0a127qouctumjuhftnb4.png)
In the extended mode, you cannot choose two non-continues values at once. Example, you cannot choose only Haskell and Julia in the above program. 
 
> For displaying the contents we will require a better method, like for example textbox. We will need to extract out all values out from the tuple, or convert it out into a string before displaying it.
____
