# [Learning Python- Intermediate course: Day 9, Complex numbers part 1](https://dev.to/aatmaj/learning-python-intermediate-course-day-9-complex-numbers-part-1-2pkh)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-9-complex-numbers-part-1-2pkh)

Today we will learn about complex numbers in Python by importing the `cmath` module.
---
____
Handling complex numbers in Python is very easy. We can easily do normal stuff like addition and subtraction, etc. without using any functions!. Complex numbers have their use in many applications related to Mathematics or algorithm based problems. They provide an excellent alternative to coordinates or vector systems.

 The `cmath` module provides useful functions to handle complex numbers and their properties. The good thing is that the module is already inbuilt and preinstalled in Python. So no need to download and install any third party add-ons! The `cmath` module is very similer to math module, but has the functionality to handle complex as well as real numbers. You will find the entire documentation [here](https://docs.python.org/3/library/cmath.html)


In case you want to check out how tedious it is to implement complex numbers in Java, you might like [this repository](https://github.com/Aatmaj-Zephyr/Complex-numbers/blob/34c51dbb570c50a93d386d5d6d45e5a3d2e6048d/Complex.java). This repository contains a class "Complex", which is the implementation of complex numbers. You can call the constructor to make complex numbers. This class also contains many useful methods to operate on complex numbers.


### Making complex numbers. 
We can make a complex number x+iy by using the following syntax
```python
z= complex(x,y)
```
Let us now create a few complex numbers.
```python
>>> import cmath # importing "cmath" for complex number operations
>>> x=2
>>> y=3
>>> z=complex(x,y)
>>> z
(2+3j)
```

### Real and imaginary parts of Complex numbers.
The real and the imaginary parts of the complex numbers can be obtained by `z.real` and `z.img`
```python
>>> z.real
2.0
>>> z.imag
3.0
```
Let us now see a full fledged program
```python

import cmath
x = 5
y = 3

# converting x and y into complex number
z = complex(x,y);

print ("The real part of complex number is : ",end="")
print (z.real)

print ("The imaginary part of complex number is : ",end="")
print (z.imag)
```
```
The real part of complex number is : 5.0
The imaginary part of complex number is : 3.0
```
### Operations on Complex numbers.
Let us now see how to do the usual operations on complex numbers. Those who are unfamiliar with math behind the operations may check [this](https://www.varsitytutors.com/hotmath/hotmath_help/topics/operations-with-complex-numbers) out

```python
>>> a=complex(2,3)
>>> b=complex(4,5)
>>> a+b 
# Adding two complex numbers
(6+8j)
>>> a-b 
# Subtracting two complex numbers.
(-2-2j)
>>> a*2
 # Multiplying complex number by a scalar
(4+6j)
>>> a*b 
# Product of two complex numbers
(-7+22j)
>>> b/4 
# Scalar division of complex number
(1+1.25j)
>>> a/b 
# Dividing two complex numbers
(0.5609756097560976+0.0487804878048781j)
>>> 1/b 
# Reciprocal of a complex number.
(0.09756097560975611-0.12195121951219513j)
>>> a**2
 # Squaring a complex number
(-5+12j)
>>> a**b
# Complex number to a complex power
(-0.7530458367485594-0.9864287886477446j)
>>> a//2 
# Invalid operation of Dividing and rounding off complex numbers.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't take floor of complex number.
```
____
