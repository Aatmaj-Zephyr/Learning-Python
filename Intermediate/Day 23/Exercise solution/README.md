# [Learning Python- Intermediate course: Day 23, IntVar() and Radio-buttons.](https://dev.to/aatmaj/learning-python-intermediate-course-day-23-intvar-and-radio-buttons-164k)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-23-intvar-and-radio-buttons-164k)

We will study radio-buttons in Tkinter in this part
---
____
Today we will create another simple program. The layout will consist of one label and four radio-buttons. The user has to choose any one of the four buttons and choose the favorite programming language.


![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qsj3kipt7kffkea7lm79.png)
 

### Intvar()
Before we start coding the program, we need to understand what is 'Intvar'. Yesterday we saw that Boolean values are not directly supported in Tkinter. We had originally written a function with Boolean values, but then had to replace it. We had to use something called as 'BooleanVar()'. But what exactly was it? Let's understand in depth today......

____
Tkinter widgets (like buttons) take input from the user. This input must be processed by the program. In order to do so, they need to 'store' the data into variables, which can be accessed by other functions in the program. But the problem with Tkinter is that Tkinter doesn't support our usual primitive data types. It's not possible to hand over a regular Python variable to a widget as a variable. So what do we do? We pass an object which does this work. These objects act as variables. The only difference is that you need to use the `get()` and `set()` methods for operating on them. To read the value of the variable, use `get()`. To put the value into the variable, use `set()`

There are four types of such Tkinter variable objects-
```python
x = StringVar() # Holds a string; default value ""
x = IntVar() # Holds an integer; default value 0
x = DoubleVar() # Holds a floating point integer ; default value 0.0
x = BooleanVar() # Holds a Boolean, returns 0 for False and 1 for True
```

The command prompt example below will make things clear.
```python
>>> a=IntVar() # You cannot declare a IntVar() without importing Tkinter
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'IntVar' is not defined

>>> from tkinter import *
>>> a=Intvar() # mind the Spelling!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Intvar' is not defined
>>> a=IntVar() # You cannot declare a IntVar() before creating a Tk() instance.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\aatma\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 539, in __init__
    Variable.__init__(self, master, value, name)
  File "C:\Users\aatma\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 346, in __init__
    master = _get_default_root('create variable')
  File "C:\Users\aatma\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 297, in _get_default_root
    raise RuntimeError(f"Too early to {what}: no default root window")
RuntimeError: Too early to create variable: no default root window
>>> master=Tk() # A blank Tkinter window opens 
>>> a=IntVar() #IntVar() is a class and we are creating an instance of the class.
>>> a.set(1) #set the value of a to 1
>>> a.get() # get (return) the value of a.
1
>>> a+2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'IntVar' and 'int'
>>> a.get()+2
3
>>> b=BooleanVar()
>>> b.set('True') # set b to 'True'
>>> b.get()
True
>>> c=DoubleVar()
>>> c.get()
0.0
>>> c.set(3)
>>> c.get() #automatic float conversion
3.0
>>> a.get()+c.get() # type converts to floating point automatically when float and integer added.
4.0
>>> d=StringVar()
>>> d.set("hello")
>>> str(c.get())+d.get() # the returned values can be used in operations.
'3.0hello'
>>> a.set(b.get()) # true=1
>>> a.get()
1
>>> a.set(c.get()) # type conversion automatic
>>> a.get()
3
>>> a.set(2.9) # floating points truncated.
>>> a.get()
2
>>> a=d
>>> a.get()
'hello'
```
Hope things are clearer now. Once we cover object oriented programming, we too will be creating objects like intvar and many more.
#### Exercise- What went wrong in the example below???
```python
>>> a=IntVar()
>>> a=1
>>> a.set(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'set'
```

[Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/a70d927e9a9551d32979e7929689b9465f9e12dd/Intermediate/Day%2023/Exercise%20solution/Exercise%201.md)

## The final program.
The final program is very easy to understand, now that we have covered `Intvar()`. Majority of the steps are the same as yesterday, with radio-buttons replacing checkboxes. So please study the program carefully and master Tkinter Radio-buttons. Comments are put wherever required.

```python
from tkinter import *
master= Tk()
master.title("RadioButton Demo...")
master.geometry("300x200")
v = IntVar()
v.set(-1) #initializing the choice, i.e. no default choice

languages = ["Python","Java","Swift","JavaScript"]
# making an array to choose the programming languages from

Stringlbl="My Favourite programming language is.... "
# text to display in the label

def showchoice(): # function to display the result
     ResultLabel.config(text= Stringlbl +languages[v.get()])

ResultLabel=Label(master,text=Stringlbl)
# Make the label                  
ResultLabel.pack()

#Set the radiobuttons
Radiobutton1=Radiobutton(master,text=languages[0],variable=v,command=showchoice, value=0)
Radiobutton2=Radiobutton(master,text=languages[1],variable=v,command=showchoice, value=1)
Radiobutton3=Radiobutton(master,text=languages[2],variable=v,command=showchoice, value=2)
Radiobutton4=Radiobutton(master,text=languages[3],variable=v,command=showchoice, value=3)

Radiobutton1.pack()
Radiobutton2.pack()
Radiobutton3.pack()
Radiobutton4.pack()                

master.mainloop()                  
```
#### Default value is not present.


![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cf3f2l0lvzjmkaatekbt.png)


If you wanted to have any default value, the you need to set v to 0 (for 'Python'.., etc) while initializing, and run the  `showchoice()` function once. If you do not run the `showchoice()` function, then Python will be selected default but the label won't show the value.


### Choosing only one among all....


![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/iln9ozktxek2xdfdtjdk.png)


![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dk3id3wppbuzpy6um10w.png)
 
_____
