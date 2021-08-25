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
