>>> import decimal 
# You must import the entire module with a astrix sign
>>> Decimal(1.1)+Decimal(2.2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Decimal' is not defined
>>> from Decimal import * 
#decimal module name is small case
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'Decimal'
>>> from decimal import *
>>> decimal(1.1)+decimal(1.2)
#`Decimal()` method is upper case
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
