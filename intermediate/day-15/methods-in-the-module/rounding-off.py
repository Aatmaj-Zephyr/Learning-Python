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
