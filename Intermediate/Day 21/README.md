# [Learning Python- Intermediate course: Day 21, Hello world in Tkinter !](https://dev.to/aatmaj/learning-python-intermediate-course-day-21-hello-world-in-tkinter-g1n/edit)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-21-hello-world-in-tkinter-g1n/edit)

Today we will write hello world in Tkinter 🤘
---
____
> Recap: Tkinter is an inbuilt python library for handling GUI. More about it [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-17-tkinter-a-fast-and-easy-way-to-create-gui-applications-1if)

### Creating a blank window
First we will create a blank window in Tkinter.
```python
import tkinter
master=Tk()
master.geometry('400x200+100+100')
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uryxfpihfrh9gikays34.png)

Explanation-
- `import tkinter` We first import Tkinter. We can also use `import tkinter as tk` or `from tkinter import *` to reduce the typing 'tkinter.abc()' everytime.

- `master=Tk()` Create an instance of Tkinter frame or window. Here 'master' is an instance of the window object.

- `master.geometry('400x200+100+100')` Set the geometry of Tkinter frame. We will understand what the parameters mean in a moment.

#### Setting the geometry.
The geometry attribute of the Tkinter consists of four parts. The first two parts (separated by `x`) denote the dimensions of the frame. Changing these values will change the default dimensions of the frame.

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ebq0vk0zfiud0dfj1j1z.png)
 
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/plyezo1dwtr33z677r7j.png)


The next two parameters (separated by +) represent the coordinates at which the frame appears on your screen. We can skip these two parameters and go by the default values.  Although we can resize and reposition the frame using the cursor, presetting values of the frame helps while setting the user experience.

### Setting title to the frame.
Till now, the frame had  the default title as 'tk'. We will now change the title to 'My First Program'
```python
import tkinter
master=tkinter.Tk()
master.geometry('300x100')
master.title("My First Program")
```


![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1akl11pqz9d43fn5ay7m.png)
 
#### Adding text to the window. 
We can add text to the window using the label widget. The label widget here takes two parameters. One of them is the text we want to input while other is the instance of the frame. (that is the `Tk()` instance). After we do that, we then need to place the widget in a proper coordinate on the frame. We do that using the `place()` attribute. The place attribute takes two inputs, the x and the y values of the coordinates. `place(x = 150, y = 150)`
```python
import tkinter
master=tkinter.Tk()
master.geometry('300x300')
master.title("My First Program")
label = tkinter.Label(master, text = "Hello world").place(x = 150, y = 150)
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hfeorjvm4170kodbem6a.png)

Forgetting the place() attribute will not display the text 

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dziorbl0oocirm4dstm9.png)
 

____
So friends we have successfully understood and completed the 'Hello world' program in Tkinter! More exciting UI to come, as the journey continues...


 
