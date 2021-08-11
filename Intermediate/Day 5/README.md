# [Learning Python- Intermediate course: Day 5, Exploring the math module](https://dev.to/aatmaj/learning-python-intermediate-course-day-5-exploring-the-math-module-5alo)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-5-exploring-the-math-module-5alo)

Today we will study how to import modules in Python, and explore the math module. 
---
_____
### What are  modules?
A module is a python file containing Python definitions and statements. A module  it must end with the `.py` extension like all other Python files. 

A module is basically a bunch of functions, variables and runnable  code. By grouping code into modules makes the code easier to read, logically understandable and enhances flexibility.
You can get the official documentation of modules [here](https://docs.python.org/3/tutorial/modules.html)

We will learn to create our own modules in the later parts, but today we explore one of the very useful Python module, that is the `math` module.

### Importing modules.
For using the math module, we just need to type `import math`, and you are set to go! You can import any Python module using the import statement.

### The math module
The math module in Python is a very useful module which lets us use mathematical functions in Python. It contains many useful mathematical functions and some constants. You can check the whole list [here](https://docs.python.org/3/library/math.html#math.log)

Here I am presenting some of the very commonly used functions.
```python
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
>>> math.atan(a) # hyperbolic trigonometric functions
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

```




