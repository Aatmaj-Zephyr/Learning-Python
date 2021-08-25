# [Learning Python- Intermediate course: Day 14, Introduction to the Decimal module](https://dev.to/aatmaj/learning-python-intermediate-course-day-14-introduction-to-the-decimal-module-4ngc)


Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-14-introduction-to-the-decimal-module-4ngc)


Today we will cover a gist of the decimal module in Python.
---
____
The Decimal module is a very vast module with a huge amount of functions. In this course, only a basic idea about the module will be given. Those who want to learn about it in depth would like to visit the [Official documentation of the decimal module](https://docs.python.org/3/library/decimal.html#) The documentation is quite easy to understand and covers everything related to the module.

> "Computers must provide an arithmetic that works in the same way as the arithmetic that people learn at school."- excerpt from the decimal arithmetic specification.

The Decimal module is a way by which faster and accurate floating point arithmetic can be achieved.

Let us take a few simple calculations on the Python command prompt
```python
>>> 1.1+3.2
4.300000000000001
>>> 1.001+2.002
3.0029999999999997
>>> 0.2+0.2+0.2-0.6
1.1102230246251565e-16
>>> 0.1+0.2+0.3-0.7
-0.09999999999999987
```
Strange eh?
Such ambiguities often arise when performing floating point arithmetic. Let us now see how to do these calculations 'properly' using the decimal module.
```python
>>> from decimal import *
>>> Decimal(1.1)+Decimal(2.2)
Decimal('3.300000000000000266453525910')
>>> getcontext().prec=2
>>> Decimal(1.1)+Decimal(2.2)
Decimal('3.3')
>>> getcontext().prec=4
>>> Decimal(1.1)+Decimal(2.2)
Decimal('3.300')
>>> int(Decimal(1.1)+Decimal(2.2))
3
>>> float(Decimal(1.1)+Decimal(2.2))
3.3
>>> print(Decimal(1.1)+Decimal(2.2))
3.300
```
Explanation. 
We first import the module using `from decimal import *` Or we can simply `import decimal` and type in `decimal.Decimal` every time we want to use it. 
> `from decimal import *` a way by which we can use everything in the module. We do not require to import a specific function from the module, but we import the entire module itself. More about importing [here](https://www.quora.com/What-does-from-import-in-Python-mean). 

When we do decimal operations, we can set the precision by giving value to `getcontext().prec` This sets the value of the precision accordingly.

When we say `Decimal(2.2)` we are creating a decimal object, with the value 2.2. One important thing to note here is that 2.2 is not of the type float, but of the type `Decimal` The cool fact is that we can directly operate on them using our arithmetic operators. 

The result has the precision equal to what we have set. But the result is of the type Decimal object. We can convert it into floating point or int data types. The print() method automatically converts the Decimal "data type" (object) into a readable string.

Some common mistakes while importing the decimal module
```python
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
```
____

So that was all we would like to cover in the decimal module.
You might like to visit [this link](https://www.tutorialspoint.com/decimal-functions-in-python) for learning about more functions or check out the [official documentation](https://docs.python.org/3/library/decimal.html#)


**Exercise**- Check out the `as_tuple()`, 'sqrt()` and the `normalize()` methods from the official documentation. Out of them, the most interesting method is the `as_tuple()` method. It is very useful when it comes to separating a decimal number into digits. The method returns a tuple containing sign, digits and the exponent value of the decimal. Note that in the sign field when the number is 0, it means the decimal is positive, when it is 1, it represents the negative number.
