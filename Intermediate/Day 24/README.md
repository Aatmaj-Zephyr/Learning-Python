# [Learning Python- Intermediate course: Day 24, Summary of the week and Adding Colors](https://dev.to/aatmaj/learning-python-intermediate-course-day-24-summary-of-the-week-and-adding-colors-238g)

Originally opublished on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-24-summary-of-the-week-and-adding-colors-238g)

Today we will check how to add background color to the widgets
---
____
### Setting the background color.
We can set the background color of the window as well as the widgets using the `bg` attribute. 
```python
from tkinter import *
master= Tk()
master.title("Color Demo...")
master.geometry("300x200")
master.configure(bg='pINk') # Not case sensative


```
The string is not case sensitive.
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/t2s1o89y1k9kcnowzpqe.png)

____
We can set the background color of the widgets in the same manner 
```python
from tkinter import *
master= Tk()
master.title("Color Demo...")
master.geometry("300x200")
master.configure(bg='pINk') # Not case sensative

a=Label(master,text="Welcome",bg="yellow")
a.pack()
master.mainloop()

```
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4r5uk0mlcspozn56ahm7.png)
 

____
#### Setting the font color

The font color can be set using the `fg` attribute. This is just the same as the `bg` attribute
```python
ResultLabel=Label(fg="Pink", text="...")
```
____
### Program to implement colors.
Let us now build a program, the same one as yesterday. A color will be chosen from the radio-buttons instead of programming languages. The background color of the Label will be accordingly to the color chosen.
```python
from tkinter import *
master= Tk()
master.title("Color Demo...")
master.configure(bg='pINk') # Not case sensative
master.geometry("300x200")


v = IntVar()
v.set(-1) #initializing the choice, i.e. no default choice
colors = ["Blue","Green","Red","Yellow"]
# making an array to choose the colors from


# text to display in the label

def showchoice(): # function to display the result
     ResultLabel.config(text=colors[v.get()],bg=colors[v.get()],fg="Orange") # set the font color to Orange.
     

ResultLabel=Label(master,font=('Helvetica', 18, 'bold '), bg="Pink", text="...")

# Make the label                  
ResultLabel.pack()

#Set the radiobuttons
Radiobutton1=Radiobutton(master,text=colors[0],variable=v,command=showchoice, fg=colors[0], bg="Pink", value=0)
Radiobutton2=Radiobutton(master,text=colors[1],variable=v,command=showchoice, fg=colors[1], bg="Pink", value=1)
Radiobutton3=Radiobutton(master,text=colors[2],variable=v,command=showchoice, fg=colors[2], bg="Pink", value=2)
Radiobutton4=Radiobutton(master,text=colors[3],variable=v,command=showchoice, fg=colors[3], bg="Pink", value=3)

Radiobutton1.pack()
Radiobutton2.pack()
Radiobutton3.pack()
Radiobutton4.pack()                

master.mainloop()   

```

Here are the snapshots-

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/893a43wxrxdx5wgxol48.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rfc81elm0m2ooxqcnuqp.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/j1ua23atexoj7siu2yie.png)
 
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1kc8gpq6awhbgysyejug.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z7uara8irpg50cz2gt5d.png)
 
_____
_____
## Summary of the week.
- [Day 21](https://dev.to/aatmaj/learning-python-intermediate-course-day-21-hello-world-in-tkinter-g1n) We learnt how to make Tkinter windows. We learnt how to set the default geometry and position of the window using the `geometry()` attribute. We made our very first 'hello world' application in Tkinter using the first widget- the Label widget.

- [Day 22](https://dev.to/aatmaj/learning-python-intermediate-course-day-22-bold-or-italics-19hg) We explored checkboxes by making a program which renders text bold, italics or both. This is achieved through the font attribute in Tkinter.

- [Day 23](https://dev.to/aatmaj/learning-python-intermediate-course-day-23-intvar-and-radio-buttons-164k) We understood the Tkinter variables `IntVar()`, `BooleanVar()`, `FloatVar()` and `StringVar()`. They are actually object instances which hold the primitive data types. They can be accessed by using their getter and setter methods. After that we made a program using Radio buttons which takes in the favorite programming language. The users can only choose one among the available options, which is the characteristic of the radiobuttons.

____
#### The `.pyw` extension

We usually store the python programs with the `.py` extensions. But this opens up a command prompt along with the file. Hence, for GUI applications, it is a good idea to name the files with an `.pyw` extension instead of a `.py` extension. This prevents the opening of the command prompt.
More about it [here](https://stackoverflow.com/questions/34739315/pyw-files-in-python-program)

