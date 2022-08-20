# [Learning Python- Intermediate course: Day 25, Buttons, Entry and Textboxes ](https://dev.to/aatmaj/learning-python-intermediate-course-day-25-buttons-entry-and-textboxes-2d0n)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-25-buttons-entry-and-textboxes-2d0n)

## Today we will cover three widgets, namely button, entry and textbox.

---

## The plain old button

We have covered check buttons, radio buttons and label in the previous parts. But now we will see how to make a simple clickable button.

The button widget can be created as shown `button=tk.Button(form,text="Press Me",command=cmd)`
'cmd' is the command to be executed once the button is pressed. The example below will make things clearer.

---

### Making a blank button

```python
import tkinter as tk

form=tk.Tk()
form.title("Example of Entry widget")
form.geometry('400x200')

button=tk.Button(form,text="Press Me")
button.pack()
form.mainloop()
show()
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/w22b2svmeh2ycai4tqxg.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/epcakg5pqhf555sthqdg.png)

On pressing the button, nothing happens. It is just a blank button. But now we will add a counter to count the number of times the button is pressed.

---

### Adding counter to the button.

```python
import tkinter as tk

form=tk.Tk()
form.title("Example of Entry widget")
form.geometry('400x200')
a=tk.IntVar()
def count():
    a.set(a.get()+1)
    button.config(text=str(a.get()))#don't forget the str()

button=tk.Button(form,text="Press Me",command=count)
button.pack()
form.mainloop()
show()
```

On pressing the button, the text of the button changes in accordance to the number of times the button is pressed. This is achieved by using the `IntVar()` variable.

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vzrdmqcpibwxh8zcxd3r.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/482syg5vj7gzexldbem1.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zrx6tz05d7g4qnmx7f9m.png)

---

---

## The Entry widget.

The entry widget is a single line textbox. The users can give in a single line input via this widget.
`entry = tk.Entry(parent)`
We can also add other parameters to the entry widget like color, etc. Here is an example below which demonstrates a blank entry widget.

### Blank entry widget.

```python
import tkinter as tk

form=tk.Tk()
form.title("Example of Entry widget")
form.geometry('400x200')


TB1=tk.Entry(form,width = 20)
TB1.pack()

form.mainloop()
show()
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mbtpby50gfg5u1qojvfx.png)

---

### Getting value from the entry.

The value of the text can be obtained using the `get()` function. The below example will make things very clear.

```python
import tkinter as tk

form=tk.Tk()
form.title("Example of Entry widget")
form.geometry('400x200')

TB1=tk.Entry(form,width = 20)
TB1.pack()
def show():
    button.config(text=TB1.get())
'''
The TB1.get() method returns the string value of the  text inputted into the entry widget. By using the config() method of the button, we can set the text of the button.
'''
button=tk.Button(form,text="", command=show)
button.pack()
form.mainloop()
show()
```

To process the input data, we will need the help of other widgets. Button for example. In the above example, when the button is pressed, the button text changes according to the value of the entry.

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5oognqdgj9yapvlebo2o.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/y4x0brdbpabmng97ncec.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6tx1vrflcvir6gy3iyhc.png)

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vp4fyvgntwwzp1ja6zoo.png)

---

---

## Textbox.

Textboxes are just the same as entry widgets, the only difference is that we can add multiple lines to it. Just replace 'Entry' by 'Text' and you are done!

---

### Blank textbox.

```python
import tkinter as tk

form=tk.Tk()
form.title("Example of textbox widget")
form.geometry('400x200')


TB1=tk.Text(form,width = 20)
TB1.pack()

form.mainloop()
show()
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6t7nv5a41xob5juki1ha.png)

#### Setting the text-space

Using the height and width attributes, we can set the number of input characters in each line.

```python
import tkinter as tk

form=tk.Tk()
form.title("Example of textbox widget")
form.geometry('400x200')

TB1=tk.Text(form,width = 5,height = 5)
TB1.pack()

form.mainloop()
show()

```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/olwmezxtkeovnt97hbt2.png)

---

### Getting input from the textbox.

We can get the input in the same manner. We need to specify two parameters to the get method. The start and the end parameter. `text=TB1.get(1.0, "end-1c")` will give the entire result.

```python
import tkinter as tk

form=tk.Tk()
form.title("Example of Entry widget")
form.geometry('400x200')

TB1=tk.Text(form,width = 7,height=5)
TB1.pack()
def show():
    button.config(text=TB1.get(1.0, "end-1c"))
'''
get(start, [end])
where,
start is starting index of required text in TextBox,
end is ending index of required text in TextBox
'''
button=tk.Button(form,text="", command=show)
button.pack()
form.mainloop()
show()

```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8ka7z6j5nlihj7px5tb0.png)

---

---

So friends, that was all for this part. In the next part, we will do a password management program! So stay tuned in this course!. Follow me on GitHub for updates.
