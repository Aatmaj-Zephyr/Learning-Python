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
