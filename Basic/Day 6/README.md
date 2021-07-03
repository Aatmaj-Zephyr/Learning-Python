 # [Learning Python-Basic course: Day 6, The While Loop and more questions🤓!](https://dev.to/aatmaj/learning-python-basic-course-day-6-the-while-loop-and-more-questions-k23)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-6-the-while-loop-and-more-questions-k23)

 🤟WELCOME 👍 Today is the day six of our course! 🔥 The syllabus for today is learning about the while loop  and solving some exciting questions like 👉 GCD & LCM 💎 and the Collatz Conjecture😃
---
_____
**The While Loop**-
The While Loop in Python shares a similer syntax like others. If the conditions are true, the loop is executed, else skipped over.

```python
while conditions :
 #statements executed if the conditions are true.
```
Here is an example-
```python
n=0
while n<10:
    print(n)
    n+=1
```
```
0
1
2
3
4
5
6
7
8
9
```
>Unlike C, there is no do-while in Python. Neither is switch case.

Here is a sample program to find the GCD and LCM of two numbers--
```python
n=int(input("Please enter first number "))
m=int(input("Please enter second number "))
dividend=n
divisor=m

rem=dividend%divisor
while rem>0:
    dividend=divisor
    divisor=rem
    rem=dividend%divisor
gcd=divisor
lcm=(n*m)//gcd
print("gcd= ",gcd,"  lcm= ",lcm)

```
In Python, one more thing is added known as while - else. With the else statement, we can run a block of code when the condition is false. This block is run only once. Syntax-
```python
while condition:
  #statement executed if condition is true
else:
  #statement executed if condition is false.
```
The program below will make things clear.
```python
i = 1 
while i < 10:
  print(i)
  i += 1
else:
  print("i is not less than 10 anymore")
```

Here is a sample program in which the sum of numbers is shown by both methods, for loop and while loop-
```python
n=int(input("Please enter a number "))
count=0
for i in range (0,n+1):
    count+=i
print(count)
count2=0
i=0
while(i<=n):
 count2+=i
 i+=1
print(count2)
```
```
Please enter a number 100
5050
5050
```

Here is another sample program of the Collatz conjuncture
```python
a=int(input("Please enter a number "))
while(a!=1):
    if(a%2==0):
        a=a/2
    else:
        a=3*a+1
```
One thing to note here is the indentation. If we put else in same indent level as while, it will become a while-else type of statement and will give wrong results. Hence, always be careful in matching the else statements and the corresponding indents. It is useful many times to leave space equal to four spaces or one tab in between indents to avoid confusion and make the code clear.

**Infinite Loops**-We can create infinite loops in Python using the while loop as shown
```python
while True:
 #statements
```
BOOM!!!💥 Be careful to terminate the program well while using the While loop.
We can transform the Collatz code into a infinite loop and give a breaking condition as shown-
```python
a=int(input("Please enter a number "))
while(True):
    if(a%2==0):
        a=a/2
    else:
        a=3*a+1
    if(a==1):
        break
```


Exercise-
1) Write a program to reverse a number (any-digit). [Answer here](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/9b055262ba02689148f92cd1410de617e8df2dc5/Basic/Day%206/Exercise%20solutions/Exercise%201.py)

2) Write a program to find the factors of a number using prime factorization.
[Answer here](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/edf39fadf07031b7865674b7f58624a52151414e/Basic/Day%206/Exercise%20solutions/Exercise%202.py)


3)Modify the prime number program we did in day 4 to replace for loop by while loop. [Answer here](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/7f0e2a24f2e934e4272bbe2aa283fb140bfb7277/Basic/Day%206/Exercise%20solutions/Exercise%205.py)

More questions on the 'For' loop-
1) Write a program to output the following 
```
1
2
1,2
3
1,3
1,2,3
4
1,4
1,2,4
1,2,3,4
5
1,5
1,2,5
1,2,3,5
1,2,3,4,5
```
Mind the trailing commas... [Answer here](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/3ce873a5bba4e987fea1c81187efbf4395c5e9c5/Basic/Day%206/Exercise%20solutions/Exercise%203.py)

2) **CODING CHALLENGE ⚔️**
swap two letters in the above solution to give this output-
```
1
1,1
1,2
1,2,1
1,2,2
1,2,3
1,2,3,1
1,2,3,2
1,2,3,3
1,2,3,4
1,2,3,4,1
1,2,3,4,2
1,2,3,4,3
1,2,3,4,4
1,2,3,4,5
```
[Answer here](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/bb69a9ab8e05381e6f49139541e1ceef58d94332/Basic/Day%206/Exercise%20solutions/Exercise%204.py)
____
✌️So friends that's all for now. 😊 Hope you all are having fun.😎 Please let me know in the [comment section](https://dev.to/aatmaj/learning-python-basic-course-day-6-the-while-loop-and-more-questions-k23) on dev.to. And don't forget to like the post on dev.to if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the comments below or gmail me. 😉
Thank you all👍

⭐Star this repo 🤩 and follow me for updates!🙂 👍 💥 🙏🙏🙏


___
