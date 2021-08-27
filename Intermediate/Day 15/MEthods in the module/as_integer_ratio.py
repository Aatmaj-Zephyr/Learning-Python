>>> import fractions as fr
>>> a=fr.Fraction(-1.75)
>>> print(a)
-7/4
>>> fr.as_integer_ratio(a)
# don't do this mistake.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'fractions' has no attribute 'as_integer_ratio'
>>> a.as_integer_ratio()
(-7, 4)
