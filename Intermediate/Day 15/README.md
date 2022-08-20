# [Learning Python- Intermediate course: Day 15, Complete guide to the fractions module](https://dev.to/aatmaj/learning-python-intermediate-course-day-15-complete-guide-to-the-fractions-module-4ki8)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-15-complete-guide-to-the-fractions-module-4ki8)

## Today is your complete guide to fractions in Python

---

> The fractions module provides support for rational number arithmetic.

The fractions module is yet another inbuilt module in Python. This module is very useful when we deal with floating numbers. This module converts floating numbers to more understandable fractions.

### Expressing numbers as fractions.

Every number can be represented as a fraction. _(Well any number with finite decimal places at least)_ Sometimes converting a number into fractions makes it easier to understand and easier to comprehend. This is also useful when you require to use rational arithmetic over floating point arithmetic for various mathematical or scientific work.

We can see how to use this module from the example shown below.

```python
>>> import fractions as fr
# import the fractions module
>>> fr.Fraction(1.5)
Fraction(3, 2)
>>> print(fr.Fraction(1.5))
3/2
>>> fr.Fraction(1,0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\aatma\AppData\Local\Programs\Python\Python39\lib\fractions.py", line 156, in __new__
    raise ZeroDivisionError('Fraction(%s, 0)' % numerator)
ZeroDivisionError: Fraction(1, 0)
>>>
```

The `fr.Fraction()` converts a floating number into a fraction object. The print function automatically converts the fraction object into a readable format.
When the denominator is zero, a `ZeroDivisionError` is returned

##### Here is another example, which I have _copied_ from the official documentation and _annotated it with comments_ to make it understandable.

```python
>>> from fractions import Fraction
# Import the `Fraction` part of the fraction module.
# from fractions import * will also work
>>> Fraction(16, -10)
# make a fraction with numerator 16, denominator 10 and
# reduce it to the lowest form
Fraction(-8, 5)
>>> Fraction(123)
# single numbers are represented as over denominator 1
Fraction(123, 1)
>>> Fraction()
# empty parenthesis indicates zero
Fraction(0, 1)
>>> Fraction('3/7')
# convert from a more readable string to a fraction format
Fraction(3, 7)
>>> Fraction(' -3/7 ')
# whitespaces do not matter
Fraction(-3, 7)
>>> Fraction('1.414213 \t\n')

'''
Convert the floating value into a fraction with denominator as a power of 10


If the \t\n wouldn't have been there, the result would have been as follows
>>> fr.Fraction(1.414213)
Fraction(6369049139822511, 4503599627370496)
'''
Fraction(1414213, 1000000)
>>> Fraction('-.125')
# -.125 is interpreted as -0.125
Fraction(-1, 8)
>>> Fraction('7e-6')
# Fraction constructor can take parameters in the exponential form also
Fraction(7, 1000000)
>>> Fraction(2.25)
# convert 2.25 into fractions
Fraction(9, 4)
>>> Fraction(1.1)
'''
 Error!!!
The fractions module interprets 1.1 as something else. The only way to get around this is to use the decimal module
Fraction(2476979795053773, 2251799813685248)
>>> from decimal import Decimal
#import the decimal module
>>> Fraction(Decimal('1.1'))
# convert decimal into fraction.
Fraction(11, 10)
```

# Operations on fractions.

Operating on fractions is just like operating on real numbers

```python
>>> from fractions import *
>>> a=fraction(1.25)
#Don't do this mistake of case insensitivity.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fraction' is not defined
>>> a=Fraction(1.25)
>>> print(a)
5/4
>>> b=Fraction(1.5)
>>> print(b)
3/2
>>> print(a+b)
11/4
>>> a.numerator
#return the numerator of the fraction
5
>>> a.denominator
# return the denominator of the fraction.
4
>>> a=-a
>>> a
Fraction(-5, 4)
>>> a*b
Fraction(-15, 8)
>>> a/b
Fraction(-5, 6)
>>> a-b
Fraction(-11, 4)

>>> a**b
(-2.56724389811345e-16-1.3975424859373686j)
```

# Methods in the fractions module.

The fractions module does contain a few useful methods as shown below.

- The `as_integer_ratio()` This returns a tuple two integers, whose ratio is equal to the Fraction in such a way that the denominator is positive.

```python
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
```

- The `limit_denominator()`

```python
>>> import fractions as fr
>>> b=fr.Fraction(3.141596372)
>>> print(b)
7074246125143851/2251799813685248
>>> b.limit_denominator(100)
Fraction(311, 99)
>>> b.limit_denominator(10)
Fraction(22, 7)
>>> b.limit_denominator(10000000)
Fraction(10390475, 3307387)
```

- Functions to round of the fractions. There are various functions to round off the fractions as shown below.

```python
>>> import fractions as fr
>>> b=fr.Fraction(3.141596372)
>>> b.__round__()
3
>>> b.__round__(3)
#round upto 3 digits.
Fraction(1571, 500)
>>> b.__floor__()
3
>>> b.__ceil__()
4
```

---

That's all for now. You might want to check out the [official documentation of the fractions module](https://docs.python.org/3/library/fractions.html) too!
