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
