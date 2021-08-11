>>> import math # import the math module
>>> a=2
>>> b=3
>>> c=4.4
>>> math.ceil(c) # the ceiling function in Python gives the smallest integer greater than or equal to the number.
5
>>> math.floor(c) # the floor function in Python gives the greatesr integer less than or equal to the number.
4
>>> math.factorial(b)
6
>>> math.comb(b,a) # Return the number of ways to choose a items from b items without repetition and without order.
3
>>> math.comb(c,a) #Raises TypeError if either of the arguments are not integers
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'float' object cannot be interpreted as an integer
>>> math.comb(-b,a) #Raises ValueError if either of the arguments are negative.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: n must be a non-negative integer
>>> math.gcd(a,b)
1
>>> math.exp(a) # e raised to the power a
7.38905609893065
>>> math.log(a) # logarithm to the base 10
0.6931471805599453
>>> math.log2(a) # logarithm to the base 2
1.0
>>> math.log(a,b) # logarithm to the base b
0.6309297535714574
>>> math.pow(a,b) # a^b
8.0
>>> math.sqrt(a) #square root of a
1.4142135623730951
>>> math.sin(a) # trigoonomatric functions
0.9092974268256817
>>> math.atan(a) # inverse trigonometric functions
1.1071487177940904
>>> math.degrees(a) # convert to degrees
114.59155902616465
>>> math.radians(a) #convert to radians
0.03490658503988659
>>> math.gamma(a) # gamma function.
1.0
>>> math.hypot(a,b) #hypotaneous calculation using the pythagores theorem.
3.6055512754639896
>>> math.pi # mathematical constant pi
3.141592653589793
>>> math.e # mathematical constant e
2.718281828459045
