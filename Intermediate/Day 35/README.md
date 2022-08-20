# [Learning Python- Intermediate course: Day 35, MessageBox widget](https://dev.to/aatmaj/learning-python-intermediate-course-day-35-messagebox-widget-19c8)

Originally oublished on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-35-messagebox-widget-19c8)

## Today we will cover message box widget in Python

---

### The messagebox widget

The messagebox widget is a widget which is used to represent pop-up message in a Tkinter program.

The program below shows an example of a simple messagebox.

```python
from tkinter import messagebox
from tkinter import *
master = Tk()
master.geometry("100x100")
def showmessage():
   messagebox.showinfo("Say hello","Hello programmers")
button=Button(master,text="Show message",command=showmessage)
button.pack()
master.mainloop()

```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nnjugbuk0l1i3vu28rjs.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fzietmvdtn232g0ltkg1.png)

**Syntax**- messagebox.showinfo(title,message)

---

Similarly The message box has different flavors of boxes

- `showinfo`- show message on popup
- `showwarning`- show warning (with disclaimer sign)
- `showerror`- Show error (with red cross)
- `askquestiion`- Asks the user yes or no
- `askyesno`- same like `askquestion`
- `askokcancel` Asks the user ok or cancel
- `askretrycancel` asks the user retry or cancel

---

### Warning

```python
from tkinter import messagebox
from tkinter import *
master = Tk()
master.geometry("100x100")
def showmessage():
   messagebox.showwarning("Wait!","Something is missing")
button=Button(master,text="Show message",command=showmessage)
button.pack()
master.mainloop()

```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wyxod4ebuia4zgdryx1b.png)

---

### Showing error

```python
from tkinter import messagebox
from tkinter import *
master = Tk()
master.geometry("100x100")
def showmessage():
   messagebox.showerror("Error!","Something is wrong")
button=Button(master,text="Show message",command=showmessage)
button.pack()
master.mainloop()
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dfyc1dmeem08lab41d4k.png)

---

### Asking question

Asking question is quite similar to `askyesno`. Both give the same output

```python
from tkinter import messagebox
from tkinter import *
master = Tk()
master.geometry("100x100")
def showmessage():
   messagebox.askquestion("stop!","are you sure?")
button=Button(master,text="Show message",command=showmessage)
button.pack()
master.mainloop()


```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7i3puhnh5fr6bv4k4smu.png)

```python
from tkinter import messagebox
from tkinter import *
master = Tk()
master.geometry("100x100")
def showmessage():
   messagebox.askyesno("stop!","are you sure?")
button=Button(master,text="Show message",command=showmessage)
button.pack()
master.mainloop()


```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4jrycce3l7ch5w94cn8a.png)

---

### Extracting values from the answer

We can get the values of the user entered answer in form of true or false from the user as shown in the program below

```python
from tkinter import messagebox
from tkinter import *
master = Tk()
master.geometry("100x100")
def showmessage():
   a=messagebox.askyesno("stop!","are you sure?")
   #returns true or false

   button.config(text=a)

button=Button(master,text="Show message",command=showmessage)
button.pack()
master.mainloop()


```

On clicking yes,

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zw58h23h4ww7weq77rok.png)

On clicking no

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mdh6euvbsdgvjdz5o8c1.png)

---

### Ask ok, cancel

```python
from tkinter import messagebox
from tkinter import *
master = Tk()
master.geometry("100x100")
def showmessage():
   a=messagebox.askokcancel("stop!","Do it?")
   #returns true or false

   button.config(text=a)

button=Button(master,text="Show message",command=showmessage)
button.pack()
master.mainloop()


```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1o9upd00p1pc4ktvp34y.png)

We can get the values from the box in the same manner as `askyesno`

---

### Ask Retry cancel

```python
from tkinter import messagebox
from tkinter import *
master = Tk()
master.geometry("100x100")
def showmessage():
   a=messagebox.askretrycancel("stop!","Action failed?")
   #returns true or false

   button.config(text=a)

button=Button(master,text="Show message",command=showmessage)
button.pack()
master.mainloop()


```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2idzgd2z314rgabsuays.png)
