# [Learning Python- Intermediate course: Day 2, returning values from methods.](https://dev.to/aatmaj/learning-python-intermediate-course-day-2-returning-values-from-methods-4bhn)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-2-returning-values-from-methods-4bhn)

Today we will learn how to return values from user defined functions.
---
____
In the [previous part](https://dev.to/aatmaj/learning-python-intermediate-course-day-1-user-defined-functions-1kg7), we covered user-defined functions which did not return any value. But today we will learn how to make functions that return Python data types. This means that now instead of just printing the values, we will now use them in our main code!

### Returning values.
When we say return a value, it simply means- give the final result back to the part of code which called the function.
The return statements can be only called from within a function. After the return statement is called, the function code terminates. This means that the statements after the return statement are not run!
Here is the syntax
```
def fun(..,..,..):
    ...
    ...
    ...
    return ...

```
#### Sample question - Write a function isodd() to check parity of numbers.
```python
def isodd(a):
    if(a%2==0):
        return True
    else:
        return False
print(isodd(5))
```
```
False
```
Run the code yourself and check for different values.

#### Exercise 1- What will happen if the else statement is removed in the above code? [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/cdf5cd5424ec5c5b6bd9fc0d05a9ddac42bcc17b/Intermediate/Day%202/Exercise%20solutions/Exercise%201.md)
____
### Returning multiple values
We cannot directly return multiple values in Python, but there are many [hacks](https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/) The best among them is returning a list of values.
#### Sample question 2- Write a function to return the smallest two entries from a given list
```python
def SmallestTwo(a):
    a.sort()
    return [a[0],a[1]]
myList=[1,4,13,7,5,9,12,3,6]
print(SmallestTwo(myList))
```
```
[1, 3]
```
### Exercise 2- Write a function to reverse a string. [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/77f9ed8e74f21dbadd14e9296a093338a113558e/Intermediate/Day%202/Exercise%20solutions/Exercise%202.py)
