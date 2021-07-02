# [Learning Python- Basic course: Day 4, The for loop](https://dev.to/aatmaj/learning-python-basic-course-day-4-the-for-loop-40m8)
Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-4-the-for-loop-40m8)

🤟Welcome all to the day 4 of our course. Today we will learn about the for loop and all it's pitfalls.😀
---
____
**Loops in python**
**The For loop**- Everyone knows that the For Loop is a type of loop which runs statements for a given number of times. Here is the for loop syntax-
````python
for i in range (0,k):
 #statement 
#the statement will run k times
```
Again, no curly braces, just indention.
Here is a sample program which prints hello five times. Note the mistakes often made by beginners.
```python
>>> for i in range (0,5) #don't forget the semicolon
  File "<stdin>", line 1
    for i in range (0,5)
                        ^
SyntaxError: invalid syntax
>>> for i in range (0,5):
... print("hello") #don't forget the indent
  File "<stdin>", line 2
    print("hello")
    ^
IndentationError: expected an indented block
>>> for i in range (0,5):
...  print("hello")
...
hello
hello
hello
hello
hello
```
Okay, the running variable i is incremented by 1. So until i equals five, the program keeps on running? Well, actually no. 😲 This happens in Java and C. But Python differs a bit over here.

In Python, the running variable is assigned a new value and not incremented. 😮 What happens is something like this- When you say "for i in range(5)", a list of numbers from zero to four [0, 1, 2, 3, 4] will be generated. (Note 0-4 and not 0-5). Then i will be assigned all the values from that list, in order, one by one. Even if we change the value of i in the middle, it doesn't affect the loop as i is just assigned the next value. more about it [here](https://stackoverflow.com/questions/15902835/changing-iteration-variable-inside-for-loop-in-python) I know, loss of flexibility.😢 But we can always convert the for loop into a while loop. 🙃 


```python
>>> for i in range (0,5):
...  i=0
...  print("hi")
...
hi
hi
hi
hi
hi
```

Although we cannot change the running variable, there is no restriction against using it. If we want to change the default value of increment of i in the list, we can add another parameter in the for loop, as shown below.

```python
>>> for i in range (0,10,2): #here 2 represents the increment values.
...  print(i)
...
0
2
4
6
8
```
Here is a sample program to find factors of a number. There are two bugs in the program. Can you fix them? 🥳
```python
n=int(input("Enter a number"))
for i in range (0,n):
  if n%i==0:
    print(i)
```
If you have already spotted them, comment the answers below👇. For those who havent, the answer is [here](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/9ad617687edd015e156cd6e3682c1a8eff704dca/Basic/Day%204/Exercise%20solutions/Exercise%201.py)

The range() function makes a list of values, and the running variable is assigned the values one by one. We can also make a list manually, but that part is to be covered when dealing with Python lists, later 📅.

 One thing to note here is that any changes in the  variable indicating the end values doesn't affect the main program. 😐Example, in the above program if we change the value of n in the indent, it wont affect the number of times the statements are executed. This is because the range list is made already using the value we have given at the time of generating the for lop. Here is a program in which the values of end variable are changed, but the program won't get affected. 🤓

```python
#Program to find the factorial of a number
a=int(input("Enter a number "))
for i in range (1,a):
    a=a*i
print(a)    
```

**Break statement**- The break statement is used to end the for loop in middle. After this statement is executed, the last for loop terminates, and the control goes to the next statements
Similarly Python has the continue statement, which starts the next iteration of the loop again. Syntax is as follows-
```Python
break
continue
```
For those who are new to the concept, you will find a really good explanation [here](https://www.programiz.com/python-programming/break-continue). 
Here is an example- This program finds if a number is prime or not.
```Python
a=int(input("Enter a number "))
IsPrime=0
for i in range (2,a//2):
    if (a%i==0):
        print("The number is composite ")
        IsPrime=1
        break
if (IsPrime==0):
 print("The number is prime.")
```

Don't get disheartened if all things are not clear right away. We are going to solve many more sample questions in the next lectures. 😎 Do try these exercises given below, (or at least see the answers). This will help strengthen the concepts or reinforce them further. 💥
 
Exercise-
2) Write a program to calculate the factors, the sum of the factors and the number of factors of the number. [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/00fa89c2d1acbc38ef381d33cf6a4da3da253267/Basic/Day%204/Exercise%20solutions/Exercise%202.py)
3) Write a program to find if a number is a perfect number or not. (Perfect number is a number whose sum of factors excluding itself is equal to number eg 6,28 are perfect numbers) [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/a3ae9361a8cf54c870d9bb6b6f31061858a03333/Basic/Day%204/Exercise%20solutions/Exercise%203.py)

____
Yes, these exercises were repetitive.🥱 But tomorrow we will do some really fantastic questions which actually are asked in interviews. Follow me for updates so you don't miss out on tomorrows special edition of learning Python course 😁. 
😉

😎 Your suggestions motivate me, so please please please let me know in the comment section if you this part or not. 🧐 And don't forget to like the post if you did. 😍 
