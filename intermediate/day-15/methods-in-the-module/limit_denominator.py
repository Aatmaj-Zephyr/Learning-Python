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
