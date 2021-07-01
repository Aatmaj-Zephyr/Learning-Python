# [Learning Python- Basic course: Day 3, Operators and If-elif-else](https://dev.to/aatmaj/learning-python-basic-course-day-3-operators-and-if-elif-else-51cc)
---
Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-3-operators-and-if-elif-else-51cc)

🤟Welcome all to the day 3 of our course. Today we will learn about operators and the if-else control flow.
---
____
**Operators in Python**-
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/t2s4qfh40fnlluqj5vro.png)
 
Operators in Python are nearly the same that of other languages like C or Java.

There are, although a few differences as highlighted below-
1) The // operator is added in Python. This operator divides the number and rounds it down to the nearest integer. 
2) The ** operator is the exponentiation operator, which raises the number to the power of a number.
3) The //= and **= assignment operators have also been added similarly. (For those unfamiliar with the assignment operators, x+=1 is equivalent to x=x+1 and so on for other signs)
4) Logical operators too exist in Python, but unlike symbols &,|,! in C, they are replaced by "and", "or", "not" in Python. This again makes it easier to read and comprehend


*Bitwise operators are similer as C, though not used much. Membership and identity operators will be covered later along with lists.*
```
>>> #Arithmatic operators
>>> a=2
>>> b=3
>>> a+b
5
>>> a-b
-1
>>> a/b
0.6666666666666666
>>> a//b
0
>>> a*b
6
>>> a**b
8
>>>#Assignment operators
>>> a=+1
>>> a
1
>>> a=2
>>> a=+1
>>> a
1
>>> a=a+1
>>>
>>> a+=1
>>> a
3
>>> a-=2
>>> a
1
>>> a*=3
>>> a
3
>>> a/=3
>>> a
1.0
>>> b**=3
>>> b
27
>>> b//=2
>>> b
13
>>> #relational operators
>>> 1>2
False
>>> 1<2
True
>>> 1==2
False
>>> 2==2
True
>>> 2!=3
True
>>> 3!=3
False
>>> 3>=3
True
>>> 3<=3
True
>>> #logical operators
>>> 1==2 and 2==2
False
>>> 1==2 or 2==2
True
>>> 1<2 and 2<3
True
>>> not 2==3
True
>>> not 2==3
True
>>> (1<2 and 2<3 ) or 3==4
True
```
____
**if-else in python.**
The if else statement works as follows-The "if" condition is checked, if the condition unsatisfied, the actions in the indentation are skipped and if "else" succeeds the "if" condition, then the statements below "else" are executed if. 
Logic of the if-elif-else statement-
```python
if condition_1:
#execute if condition_1 is True
...
elif condition_2:
#execute if condition_1 is false and condition_2 is True
...
else:
#execute only if both condition_1 and condition_2 are False
...
```

Unlike C, in Python we do not have to cover the conditions in any parentheses. However I personally feel that the brackets feel neat if added and prevent any confusion. The curly braces in C are replaced by indentation in Python. The "elif" in Python is same as else if in other languages.


Here is a sample program which checks if a number is positive, negative or zero.
```python
a=int(input("Enter a number "))
if a>0:
 print(a,"is a positive number")
elif a<0:
 print(a,"is a negative number")
else:
 print(a,"is zero")
```

Another sample program to find the number of digits of a number not more than 5 digits.
```python
a=int(input("please enter a number "))
if(a<10):
    print(" 1 digit number")
elif(10<a<100):
    print(" 2 digit number")
elif(100<a<1000):
    print(" 3 digit number")
elif(1000<a<10000):
    print(" 4 digit number")
else:
    print(" 5 digit number")
```
 Execise- 1) There is a bug in the sample program for finding number of digits. Can you fix it? [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/b628c3aa0bee60b75747dc3caff95b57485668fd/Basic/Day%203/Exercise%20solutions/Exercise%201.py)
          2) Modify Sample program 1 to print if a number is odd even along with positive and negative. [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/b628c3aa0bee60b75747dc3caff95b57485668fd/Basic/Day%203/Exercise%20solutions/Exercise%202.py)
          3) Quadratic equation- values of a,b,c are entered by the user. Find any one root if exists, else print doesn't exist. [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/0662136141e77e25dc540b38fc31f03e965d4901/Basic/Day%203/Exercise%20solutions/Exercise%203.py). This exercise will test the operators as well as the if-else.

*To be continued....😏*
____

So friends that's all for this part. 😊 Hope you all are enjoying.😎 Please let me know in the comment section if you liked it or not. 🧐 And don't forget to like the post if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the comments below or gmail me. 😉
Thank you for being so patient.👍

