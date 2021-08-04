# [Learning Python- Intermediate course: Day 1, User defined functions](https://dev.to/aatmaj/learning-python-intermediate-course-day-1-user-defined-functions-1kg7)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-1-user-defined-functions-1kg7)

Welcome all to the first part of the intermediate course! Today we will start user defined functions.
---
____

In this part, we will cover only function which do not return any value, or as per C syntax 'void' functions.

### What are user defined functions?
> User-defined functions are functions that you use to organize your code in the body.

Let's say that we want to execute a part of the code many times throughout the program. If we type the same lines of code over and over, what will happen? Not only we will waste time in typing, but the overall code structure will be almost unreadable! Moreover what will happen if you want anytime to change the way the function works! 

This is one of the many places where user defined functions come in handy. Once we tell the functions what to do, that is give them a piece of code to run, we are ready to go. We can then call them again and again with just a single line. Editing the function becomes simple and code looks compact and clean. They are an invaluable part of OOP in Python. User defined methods also allow us to use recursion, but more about that later. 

### Syntax of python functions
In order to make functions, we first need to define them. this is done using the `def` keyword. Then we need to declare input parameters to the function. Finally we put a semicolon at the end. After that, we put the code to be run in an indent. This is done as shown-

```
def fun(...,...,...):
    ...
    ...
    ...
```
Well, a practical example might be more useful-
```python
def fun(a,b,c):
    print(a+b+c)
fun(2,3,4)
fun(4,9,-1)
```
OUTPUT-
```
9
12
```
In the above program, what we have done is we have declared a function named fun, and have given it three input parameters, namely a,b and c. Then in the function code, we have told to print the sum of a, b and c.

One thing to be noted is that the **function must be declared before it is used.** If we do not follow this rule, then the code will not run. For example-
```python
fun(2,3,4)
def fun(a,b,c):
    print(a+b+c)
fun(4,9,-1)
```
OUTPUT-
```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    fun(2,3,4)
NameError: name 'fun' is not defined
```
Hence it is a good practice to declare all the functions before writing the main code. 

### Sample question 1- Write a function to check if two numbers are greater than, less than or equal to and print the values.
```python
def compare(a,b):
    if(a<b):
        print(a,"<",b)
    elif(a>b):
        print(a,">",b)
    else:
        print(a,"=",b)
compare(3,5)
compare(-2,-4)
compare(4,4)
```
OUTPUT-
```
3 < 5
-2 > -4
4 = 4
```

### Sample question 2- Write function to print the product of all the elements in a list.
```python
def prod(a):
    temp=1
    for i in a:
        temp*=i 
    print(temp)
prod([1,2,3,4])
b=[5,7,4,-2]
prod(b)
```
OUTPUT-
```
24
-280
```
### Exercise- What changes will you make to the Function to print the product if we were to put tuples instead of lists? [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/e0742533c3146fd2fc097935e67477e8ae9d1240/Intermediate/Day%201/Exercise%20solutions/Exercise%201.md)

