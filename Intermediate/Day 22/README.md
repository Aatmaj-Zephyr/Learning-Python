# [Learning Python- Intermediate course: Day 22, Bold or Italics !](https://dev.to/aatmaj/learning-python-intermediate-course-day-22-bold-or-italics-19hg)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-22-bold-or-italics-19hg)

## Today let us explore checkboxes in Python.

---

Today we are going to make a simple program which displays text in bold or italics, or both. This is a standered example for learning checkboxes. The layout will be a simple one. There will be a label which displays the word 'text'. There will be two checkboxes for bold as well as italics. When the checkboxes are clicked, then the label text must become bold or italics or both depending on the checkboxes.
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mwki45k417ovyva9dl9e.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qiqpp92br58m930e9op0.png)
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/an0mfhnfzcu116fwr462.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i4xee9x0amzp44k1ej2u.png)

### Making the label.

Just as we made a hello world label yesterday, we will make one label today. The label will have the text "text".

```python
from tkinter import *

window=Tk()
#create a window frame called master
window.title("Checkboxes")
window.geometry("250x100")

label=Label(window,text="text")
#create a label with text 'empty' and put it in the window frame
label.pack() #pack the label into the frame
window.mainloop() #halt execution and display the widgets.

```

> Yesterday we had used the place attribute to place the label in the position. But as the checkbox program has many widgets to be placed, we will use the `pack()` method. This method packs the label widget into the frame and the `mainloop()` displays them. More abot window.mainloop() [here](https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cfl5n6j4qnwuhp1fautv.png)

### Function to check and set bold and italics

We will now make a function named `ChangeLabel` to change the values of the label. For that we make two Boolean attributes, bold and italics. The function must take two Booleans as inputs and must change the value of the label.

The values of the label can be changed using the `config()` function. `label.config(text='hello')` changes the text value to hello. Similarly we can change the bold or the italics using the font attribute. `font=('Helvetica', 18, 'bold')`

After making the function, we test it for all combinations.

```python
from tkinter import *

window=Tk()
#create a window frame called master
window.title("Checkboxes")
window.geometry("250x100")

label=Label(window,text="text")
#create a label with text 'empty' and put it in the window frame

def ChangeLabel(bold,italics):
    if(bold == True and italics == False):
        label.config(text='bold',font=('Helvetica', 18, 'bold'))
    elif(bold ==False and italics == True):
        label.config(text='italics',font=('Helvetica', 18, 'italic'))
    elif(bold ==True and italics == True):
        label.config(text='bold and italics',font=('Helvetica', 18, 'bold italic'))
    else:
        label.config(text='text',font=('Helvetica', 18, ''))

bold= False
italics= True
ChangeLabel(bold,italics)


label.pack()
# The pack() and mainloop() attributes must be at the end of the program
window.mainloop()

```

---

> **Note** `pack()` and `mainloop()` attributes must be at the end of the program, else the program won't function as expected.

---

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tbjln0y60abymgcb3tyc.png)
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zv6umzpy0dn8p5w5ma91.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/iyqnnngd0iv3y48qtdc1.png)
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/51fc4bme61iomgyixkwk.png)

---

### Setting checkboxes.

We can make checkboxes with the following parameters.

```python
Boldcheckbox= Checkbutton(window,text="Bold", variable=bold,onvalue=1, offvalue=0,command=ChangeLabel)

```

- `window` : Set the window frame instance into the checkbox
- `text="Bold"` : Set the text of the checkbox
- `variable=bold` : give the checkbox a variable to change. When the button is on, the value of the bold will be set `1` and when it is off, the value will be `0`.
- `onvalue=1, offvalue=0` : Set the on and off values.
- `command=ChangeLabel` : The command to be executed

###### But before we can do use the checkbox, we need to do two important changes to our function.

#### Number one: Make the variables global.

We cannot parametrize any function in the command checkboxes. This means we cannot do `Boldcheckbox= Checkbutton(window,text="Bold",........,command=ChangeLabel(bold,italics))`
The only workaround for this is to use global variables bold and italics

#### Number two: Tkinter doesn't support Booleans!

You cannot directly change the values of the boolean variables through the buttons. `Boldcheckbox= Checkbutton(window,text="Bold", variable=bold,onvalue=True, offvalue=False,command=ChangeLabel)` fails!!

But Tkinter has a special object for handling Boolean types known as `BooleanVar()`. The BooleanVar() is an object which returns the Boolean value using the `BooleanVar.get()` method and we can set the value using the `BooleanVar.set()` method. The BooleanVar represents 1 for true and 0 for false.

---

So we will now make our function use global objects bold and italics and change the if statement. The new function is as shown.

```python
def ChangeLabel():
    if(bold.get() == 1 and italics.get() == 0):
        label.config(text='bold',font=('Helvetica', 18, 'bold'))
    elif(bold.get() ==0 and italics.get() == 1):
        label.config(text='italics',font=('Helvetica', 18, 'italic'))
    elif(bold.get() ==1 and italics.get() == 1):
        label.config(text='bold and italics',font=('Helvetica', 18, 'bold italic'))
    else:
        label.config(text='text',font=('Helvetica', 18, ''))

bold= BooleanVar()
italics= BooleanVar()
```

> BooleanVar() and other such objects will be explained in more depth in the next session

### Finally, we are there......

The entire program will become-

```python
from tkinter import *

window=Tk()
#create a window frame called master
window.title("Checkboxes")
window.geometry("250x100")

label=Label(window,text="text")
#create a label with text 'empty' and put it in the window frame

def ChangeLabel():
    if(bold.get() == 1 and italics.get() == 0):
        label.config(text='bold',font=('Helvetica', 18, 'bold'))
    elif(bold.get() ==0 and italics.get() == 1):
        label.config(text='italics',font=('Helvetica', 18, 'italic'))
    elif(bold.get() ==1 and italics.get() == 1):
        label.config(text='bold and italics',font=('Helvetica', 18, 'bold italic'))
    else:
        label.config(text='text',font=('Helvetica', 18, ''))

bold= BooleanVar()
italics= BooleanVar()
Boldcheckbox= Checkbutton(window,text="Bold", variable= bold, onvalue=1,offvalue=0,command=ChangeLabel)
Italicscheckbox= Checkbutton(window,text="Italics", variable= italics, onvalue=1,offvalue=0,command=ChangeLabel)

label.pack()
Boldcheckbox.pack()
Italicscheckbox.pack()
#pack in the order of appearance.

# The mainloop() attributes must be at the end of the program
window.mainloop()
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6yk81axuufqlwk3je024.png)

---
