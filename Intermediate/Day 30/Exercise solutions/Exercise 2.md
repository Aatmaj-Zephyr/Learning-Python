`Lb.curselection()` returns a tuple of values. This is why `Lb.curselection()[0]` is used as it returns only the first value. In the above program, we wanted only the first value to be selected, hence we used the `[0]` syntax.


Not doing so will give the error below-
```python
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\aatma\AppData\Local\Programs\Python\Python310\lib\tkinter\__init__.py", line 1884, in __call__
    return self.func(*args)
  File "C:/Users/aatma/AppData/Local/Programs/Python/Python310/lb.py", line 11, in show
    showbutton.config(text=items[Lb.curselection()])
TypeError: tuple indices must be integers or slices, not tuple
  ```
