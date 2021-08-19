# [Learning Python- Intermediate course: Day 10, Complex numbers part 2](https://dev.to/aatmaj/learning-python-intermediate-course-day-10-complex-numbers-part-2-48jh)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-10-complex-numbers-part-2-48jh)

In the last part, we learnt the basics of operating with complex numbers. Today we will cover many different functions related to complex numbers.
---
____
### Phase of complex number
The phase or the argument of  any complex number can be found out using the `phase()` function.
```python
import cmath
x = -1.0
y = 0.0
# converting x and y into complex number
z = complex(x,y);
# printing phase of a complex number using phase()
print ("The phase of complex number is : ",cmath.phase(z))
```
```
The phase of complex number is :  3.141592653589793
```
### Polar form of complex number.
We can convert a complex number to polar form using the `polar()` and back into rectangular form using the `rect()` function.
```python
import cmath
z = complex(1,1)
a = cmath.polar(z)
print ("The polar complex number is : ",end="")
print (a) # returns a tuple
z2= cmath.rect(a[0],a[1])
print ("The rectangular form of complex number is : ",end="")
print (z2)
```
```
The polar complex number is : (1.4142135623730951, 0.7853981633974483)
The rectangular form of complex number is : (1.0000000000000002+1j)
```

> Note the return types for the functions 
- `polar()` returns a tuple.
- `rect()` returns a complex number.

### Functions is the cmath module
Let us now explore the functions in the cmath module which are frequently used. The example below explains the use of the most commonly used functions. Entire list of functions with documentation can be found [here](https://docs.python.org/3/library/cmath.html)
```python
>>> import cmath
>>> z=complex(-2,1)
#make a complex number.
>>> cmath.exp(z)
# Raise z to a complex power.
(0.07312196559805963+0.1138807140643681j)
>>> cmath.exp(z.real)
# the cmath module takes in real as well as complex parameters.
(0.1353352832366127+0j)
>>> cmath.log(z,10)
#logarithm of z to the base 10
(0.3494850021680094+1.1630167557051545j)
>>> cmath.log(10,z)
# logarithm of 10 to  the base z
(0.2369795135136017-0.7886208085195003j)
>>> cmath.log(z,z)
#alogarithm of z to the base z
(1+0j)
>>> cmath.sqrt(z)
# square root of z
(0.34356074972251244+1.455346690225355j)
>>> cmath.acos(z)
# arccos of z
(2.6342363503726487-1.4693517443681852j)
>>> cmath.atan(z)
# arctan of z
(-1.1780972450961724+0.17328679513998632j)
>>> cmath.sin(z)
# arc sine of z
(-1.4031192506220405-0.4890562590412937j)
>>> cmath.acosh(z)
# hyperbolic inverse cosine
(1.4693517443681852+2.6342363503726487j)
>>> cmath.tanh(z)
# hyperbolic tangent
(-1.0147936161466335+0.0338128260798967j)
>>> cmath.pi
# The usual pi constant
3.141592653589793
>>> pow(z,z)
# z raised to the power z.(note that this is not from the cmath module.
(-0.00220568464655929+0.013562654681556313j)
```
> Note- j is often used in electronics instead of i, hence in Python expressions like `1+1i` are written as `1+ij`

____
## Applications of complex numbers to computer science.
Well I know you all must be wondering why in the world are we learning about complex numbers. Well, this is because complex numbers are a very handy tool in solving many real world problems. They are a great way to store in coordinate systems. As we just saw, they are very easy to implement than when compared to vectors. In Python, complex numbers can be operated naturally just like plain old real numbers. 

Other applications of complex numbers include-
- Signal processing
- Image processing
- Scientific computing
- Graphics
- Computer vision
- Data compression

Read also
- [What are some applications of complex numbers in computer science?](https://www.quora.com/What-are-some-applications-of-complex-numbers-in-computer-science)
- [complex numbers in programming?](https://softwareengineering.stackexchange.com/questions/118690/complex-numbers-in-programming)

____
# For those who are new to the concept of complex numbers might like the video below.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=T647CGsuOVU
"><img src="http://img.youtube.com/vi/T647CGsuOVU/0.jpg" alt="Welch labs vedio" width="240" height="180" border="10"></img></a>

_____
_____

Did You like the content?😎 Please let me know in the [comment section on dev.to](https://dev.to/aatmaj/learning-python-intermediate-course-day-10-complex-numbers-part-2-48jh) 👇. And don't forget to like the post if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the [comments on dev.to](https://dev.to/aatmaj/learning-python-intermediate-course-day-10-complex-numbers-part-2-48jh) or gmail me. 😉
Thank you all👍

Please star this repository!
