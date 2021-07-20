# [Learning Python-Basic course: Day 14, Basic Exception and error handling using try-except](https://dev.to/aatmaj/learning-python-basic-course-day-14-basic-exception-and-error-handling-using-try-except-5f38)


Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-14-basic-exception-and-error-handling-using-try-except-5f38)

Today we will cover exception handling in Python by using the `try` and `except` statements.
---
___

The `try` statement is used to prevent errors while coding. You might try to pop from an empty list, process user input character as an int or divide by zero, this statement has got you covered!.
```python
try:
 #statement1- try to execute, but if any error is returned, then do not execute
except:
 #statement2- execute if any error occurs
finally: #optional
 #Statement2- execute nevertheless
```

The `try` & `except` statements provide a robust alternative for the if-else statement. But this comes at the cost of a little more difficulty while debugging, when unexpected errors are not displayed. This is somewhat similar too the `throw` `catch` statements in C.

Here is a program which error checks if the user enters a number or not.
```python
a=input("Please enter a number ")
try:
    b=int(a)
    print(b)
except:
    print("OOPS! You entered a non-numeric character! ")
finally:
    print("End of program!")
```
OUTPUT-
```
Please enter a number 6
6
End of program!
```
```
Please enter a number g
OOPS! You entered a non-numeric character! 
End of program!
```

According to the python documentation [here](https://docs.python.org/3/tutorial/errors.html), there are three types of errors as shown-
```
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
```

We can specify multiple error handling as shown-
```python
try:
  print(x)
except ZeroDivisionError:
  print("Cannot divide by zero.")
except:
  print("Something else went wrong")
```

#### Pass statement
The except statement is compulsory, means that even if you do not want anything to happen if there is an exception, you still have to write it. Here is where the `pass` statement comes into play. The `pass` statement is basically a 'no-operation' statement in Python.
```python
try:
  #try to execute
except:
    pass
#do nothing
```

#### Exercise

1) Solve the [exercise 2 of the day 13](https://dev.to/aatmaj/learning-python-basic-course-day-13-summary-of-the-week-and-stack-implementation-1b56) using the `try` `except`. [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/60564a084135d6b25177c33a6e35a5b428b0f54e/Basic/Day%2014/Exercise%20solutions/Exercise%201.py)

____
✌️So friends that's all for now. 😊 Hope you all are having fun.😎 Please let me know in the comment section on [dev.to](https://dev.to/aatmaj/learning-python-basic-course-day-14-basic-exception-and-error-handling-using-try-except-5f38). And don't forget to like the post if you did. 😍
I am open to any suggestions or doubts. 🤠 Just post in the comments below or gmail me or fork this [file](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/main/Basic/Doubts/Doubts.md) 😉
Thank you all👍

Don't forget to star this repo too!
