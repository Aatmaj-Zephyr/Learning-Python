The following error will be generated-

```
Traceback (most recent call last):
  File "main.py", line 13, in <module>
    a.print_tax(20)
  File "main.py", line 8, in print_tax
    self.set_amount(self,amount)
TypeError: set_amount() takes 2 positional arguments but 3 were given

```

Thumb rule -> inside of another function, use a function like you would outside the class.
