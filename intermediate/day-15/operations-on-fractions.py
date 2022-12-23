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
