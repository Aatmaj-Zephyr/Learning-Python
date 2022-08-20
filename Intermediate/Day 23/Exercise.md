What is wrong in the example below?

```python
>>> a=IntVar()
>>> a=1
>>> a.set(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'set'
```
