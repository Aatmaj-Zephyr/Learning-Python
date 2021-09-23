# [Learning Python- Intermediate course: Day 29, Sliders in Tkinter](https://dev.to/aatmaj/learning-python-intermediate-course-day-29-sliders-in-tkinter-5a6d)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-29-sliders-in-tkinter-5a6d)

Today let us learn all about the slider widget in Tkinter
---
____
The slider widget is a widget that helps us choose values from a given range in a very interactive and graphical way.

### Making a slider widget.
We can make the slider widget using the following syntax
`slider=Scale(master, from_=0, to=10)` 
Parameters
- `master` The main Tk() window.
- `from_` The starting value of the slider
- `to` the ending value of the slider.

```python
from tkinter import *
frame=Tk()
frame.geometry("200x200")
slider=Scale(frame, from_=0, to=10)
slider.pack()
mainloop()
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/du3lrwjchp98k1r0tth3.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/to9jg79v0m5xa0btz2ew.png)

### Setting default value
The `slider.set()` is a method which sets the value of a slider. We can use this to initialize the default value of the slider. 
```python
from tkinter import *
frame=Tk()
frame.geometry("200x200")
slider=Scale(frame, from_=0, to=10)
slider.set(2)
slider.pack()
mainloop()
```
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3xrc9qlgnkzs6k9m0isb.png)
 

The `set()` method can also be used to dynamically set the value of the slider variable. 

The program below is an example of the set() method. There is a button which runs a function which resets the value of the slider back to the default values when pressed.

```python
from tkinter import *
frame=Tk()
frame.geometry("200x200")
slider=Scale(frame, from_=0, to=10)
slider.set(2)
slider.pack()
def reset():
    slider.set(2)
resetbutton=Button(frame, text="reset",command=reset)
resetbutton.pack()
mainloop()
```
 On pressing the reset button, the value returns back to the default value.

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/y2bjdro1dj1xd9titudg.png)
 

### Orientation of the slider.
By default, the slider is vertical. But we can use the `orient` property to set the value of orientation.
 
```python
from tkinter import *
frame=Tk()
frame.geometry("200x200")
slider=Scale(frame,from_=0, to=10, orient="horizontal")
slider.set(2)
slider.pack()
def reset():
    slider.set(2)
resetbutton=Button(frame,text="reset",command=reset)
resetbutton.pack()
mainloop()
```
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7i4ux523gdnaozry2nxc.png)
 

### Getting the value from the slider.
We can get the value of the slider using the `slider.get()` method. The program below shows how to get the values of the slider using buttons.

```python
from tkinter import *
frame=Tk()
frame.geometry("200x200")
slider=Scale(frame,from_=0, to=10, orient="horizontal")
slider.set(2)
slider.pack()
def reset():
    resetbutton.config(text=slider.get())
resetbutton=Button(frame,text="show",command=reset)
resetbutton.pack()
mainloop()
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zqn4q0faeg31m1h38qu9.png)
 
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7ruqfwcqvtxs0dlkp9zi.png)
 
### Setting the interval length
We can display the values of the sliders using the `tickinterval` property. We can adjust the interval values of the slider using the `tickinterval` attribute.  For example, setting the value to 10 equal will show the result as 

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/a1gvwrc5ojmu4cnp7id5.png)

While setting the value to 1 will show the entire range

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/a0bbmf2yc8hl4zxxru6y.png)
 
```python
from tkinter import *
frame=Tk()
frame.geometry("200x200")
slider=Scale(frame,from_=0, to=10, tickinterval=1, orient="horizontal")
slider.set(2)
slider.pack()
def reset():
    resetbutton.config(text=slider.get())
resetbutton=Button(frame,text="show",command=reset)
resetbutton.pack()
mainloop()
```


That looked a bit crowded. Didn't it? We can adjust it using the length property of the slider. 

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cs88e5zx4f7phm6h0wgh.png)
 
Here is the code-

 ```python
from tkinter import *
frame=Tk()
frame.geometry("200x200")
slider=Scale(frame,from_=0, to=10, tickinterval=1, length= 500, orient="horizontal")
slider.set(2)
slider.pack()
def reset():
    resetbutton.config(text=slider.get())
resetbutton=Button(frame,text="show",command=reset)
resetbutton.pack()
mainloop()
```
_____
