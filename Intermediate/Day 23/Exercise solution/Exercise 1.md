Due to automatic type conversion in Python. Type conversion takes place between integer and intvar.

`a=IntVar()`
a is of type IntVar()
`a=1`
a is now of type integer. (automatic type conversion of Python
`a.set(1)`
But now int has no attribute set()!
`Traceback (most recent call last): File "<stdin>", line 1, in <module> AttributeError: 'int' object has no attribute 'set'`
