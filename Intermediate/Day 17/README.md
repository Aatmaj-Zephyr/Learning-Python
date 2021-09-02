# [Learning Python- Intermediate course: Day 17, Tkinter — a fast and easy way to create GUI applications.](https://dev.to/aatmaj/learning-python-intermediate-course-day-17-tkinter-a-fast-and-easy-way-to-create-gui-applications-1if)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-17-tkinter-a-fast-and-easy-way-to-create-gui-applications-1if)

Today we will begin with GUI in Python!
---
_____
Python has a inbuilt package for GUI handling known as 'Tkinter'. This GUI toolkit is available on most Unix platforms, including macOS, as well as on Windows systems.

> Note- Tkinter provides a powerful object-oriented interface to the Tk-GUI toolkit. GUI requires a lot of OOP stuff. OOP python is still not covered in this course, and would be subsequently covered after GUI is completed. So till that time, don't worry if OOP things are not 100% clear. While learning GUI it is important to understand how to design things rather than how they are implemented by python. Learning OOP concepts will throw light upon how they are implemented and things will start getting clearer and clearer.
____
### But what is Tkinter?
  The Tkinter package is actually an interface to the GUI toolkit, called as Tk-GUI. However, Tkinter is not the only GUI Programming toolkit for Python. It is one of the most common and easy to learn interface. It is the only framework that’s built into the Python standard library. Other notable interfaces are [wxPython](https://wxpython.org/) and JPython ([Jython](https://www.jython.org/). wxPython is an open-source Python interface for wxWindows, while JPython is a Python port for Java. JPython boasts of giving Python scripts a seamless access to Java class libraries on the local machine. Other alternatives include-  [PyQt](https://en.wikipedia.org/wiki/PyQt), [PySide](https://en.wikipedia.org/wiki/PySide), [Pygame](https://en.wikipedia.org/wiki/Pygame), [Pyglet](https://en.wikipedia.org/wiki/Pyglet), and [PyGTK](https://en.wikipedia.org/wiki/PyGTK). You can check them out at the wiki links provided.

The name Tkinter comes from Tk interface. Tkinter was written by Fredrik Lundh. It is free software released under a [Python license](https://en.wikipedia.org/wiki/Python_license).

Advantages of Tkinter
- Tkinter is lightweight and a bit easier to use than others.
- Tkinter is cross-platform, so the same code works on all systems ( Windows, macOS, and Linux)
- Moreover, Tkinter elements are built using native operating system elements, So they easy camouflage to the system 


Disadvantage of Tkinter
- Tkinter is outdated... No Expired might be the right word. The UI looks old, or rather ancient. If you want to build a good looking shiny application, then Tkinter is not for you!

This is why Tkinter is ideal for just studying and exploring GUI in Python.

#### Checking if Tkinter is properly installed or not.

Let's see how to check if Tkinter is properly installed on the system, and which version is installed.
We can do that by typing the command `python -m tkinter` in the command line. This opens a small box with two buttons as shown below. Inside the box, the version of the Tcl/Tk is shown.

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ck11zv8wg3sw46bsx90c.png)


![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9kr167dc5gwoa6cvcevx.png)
 
 
> Didn't work for you? Well it didn't work for me either. 
```
C:\Users\aatma>python -m tkinter
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.
```
In my device, the `py` keyword opens python, so typing in `py -m tkinter` worked for me.
> Common mistake-- We need to type this in the command prompt, and not the python command line!

This won't work-
```
C:\Users\aatma>py
Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> python -m tkinter
  File "<stdin>", line 1
    python -m tkinter
              ^
SyntaxError: invalid syntax
```

When we click on the click me button, The click me is surrounded with square brackets as shown.


![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hbgmqgksth2riywg8k0o.png)


 Each time we click it, an additional pair of paranthesis encloses the text on the button-clickme
 
 
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/chy3zziimshi2x3p8e9c.png)


![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bdtwz2xsetocmma0yn4j.png)


Clicking the 'quit' button closes the box.
 
_____
That's all for this part. Excited? Before you even realize, we will be making applications much more powerful and exciting than this one. So stay tuned for the next parts of the [Learning Python](https://github.com/Aatmaj-Zephyr/Learning-Python) Course.

🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
Follow me on GitHub for updates.......
