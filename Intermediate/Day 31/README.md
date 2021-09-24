# [Learning Python- Intermediate course: Day 31, Coordinate positions](https://dev.to/aatmaj/learning-python-intermediate-course-day-31-coordinate-positions-4eah)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-31-coordinate-positions-4eah)

Let us now cover the coordinate layout in Tkinter
---
____

Today we will make a program which will take in inputs of principle and discount and calculate the total price.


![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fnj495lupa6i400h39fa.png)
 
Here are the program specs 
- One label for the text principle
- One label for the text discount
- One label for the total value
- One button show.
- One slider for the discount values
- One spinbox for the principle amount

Now that we have got all the specs, let's start building the program-

```python
from tkinter import *
master=Tk()
master.geometry("300x200")

Lbl1=Label(master,text="Principle")
Lbl2=Label(master,text="Discount")
Lbl3=Label(master,text="Total. ",font="20px")
spinbox=Spinbox(master,from_=10, to=100)
slider=Scale(master,from_=0, to=100, tickinterval=20, length= 150, orient="horizontal")
def display():
    a=int(spinbox.get())-int(spinbox.get())*int(slider.get())/100
    Lbl3.config(text=str(a)+"$")
button=Button(master,text="Calculate",command=display)

spinbox.pack()
Lbl1.pack()
slider.pack()
Lbl2.pack()
button.pack()
Lbl3.pack()

mainloop()
    

```


![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rehq8f29llammp8dlg39.png)
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i7s6d3swtck4fgbdeuv0.png)


The program works all right, but that's not how we want to display the widgets. We need to adjust the look and feel. We want the first two labels to be adjacent towards the spinbox and slider widgets. For that, we use the coordinate layout. The pack layout is not sufficient as it packs all the widgets into just a centre line. Hence, we will place them coordinately.  

We can set the coordinates of the widgets using the `place` method. Example `widget.place(x=30,y=20)`
Here is the final program, now with the power of place layout.

 
 
 
 
 ```python

from tkinter import *
master=Tk()
master.geometry("300x200")

Lbl1=Label(master,text="Principle")
Lbl2=Label(master,text="Discount")
Lbl3=Label(master,text="Total. ",font="20px")
spinbox=Spinbox(master,from_=10, to=100)
slider=Scale(master,from_=0, to=100, tickinterval=20, length= 150, orient="horizontal")
def display():
    a=int(spinbox.get())-int(spinbox.get())*int(slider.get())/100
    Lbl3.config(text=str(a)+"$")
button=Button(master,text="Calculate",command=display)

spinbox.place(x=100, y=0)
Lbl1.place(x=0,y=0)
slider.place(x=100, y=50)
Lbl2.place(x=0,y=70)
button.place(x=150,y=130)
Lbl3.place(x=150,y=170)

mainloop()
    
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8rg0b7xsu1eywqtt7gvd.png)
 
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/65e8z6vn5qyqmp4qss02.png)
 

One thing to note is that the layouts remain the same even if the window is resized.

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/t8u03skx2j8b91ru5hal.png)
 
