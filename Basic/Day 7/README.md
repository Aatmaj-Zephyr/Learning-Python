# [Learning Python-Basic course: Day 7, Exercises and coding challenges⚔️](https://dev.to/aatmaj/learning-python-basic-course-day-7-exercises-and-coding-challenges-2l2b)

Originally published on the Dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-7-exercises-and-coding-challenges-2l2b)

Welcome 🖐️ Today's agenda is solving more interesting questions! ❤️ intricate patterns and mind-blowing sequences ✨
---
____
Let us now today solve some more questions 😀 on while loops and for loops. 😁 We will look at 2-3 sample questions followed by exercises and a coding challenge ⚔️.

Sample questions-

1) Write a program to print Fibonacci numbers.
```python
a=0
b=1
print('0,1,',end="")
for i in range(0,10):
   a,b=b,b+a
   print(b,end=",")
```
**Simultaneous assignment of values**
Note the second last line. This is the Python syntax for simultaneous assignment. This is equivalent to using a temp variable like-
```python
temp=a
a=b
b=b+temp
```
This python shortcut comes very very handy while swapping two numbers to

2) Write a program to display times table from 1-10
```python
for i in range(1,11):
    for j in range(1,11):
        print(i,"*",j,"=",j*i)
    print()
```

OUTPUT-
```
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
.
.
.
. for numbers upto 10
```
What such a small amount of code can do in seconds took us years to learn...🤩

Exercises-

1) Modify the factorial program we did in day 4 to error check for zero and negative numbers.(using if-else) [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/15c67abac0cfe0a98dca8aca04feff544f2cc379/Basic/Day%207/Exercise%20solutions/Exercise%201.py)

2) Write a program to give the following output. [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/15c67abac0cfe0a98dca8aca04feff544f2cc379/Basic/Day%207/Exercise%20solutions/Exercise%202.py)
```
1
121
12321
1234321
```

3) Write a program to display [perfect numbers](https://www.britannica.com/science/perfect-number#:~:text=Perfect%20number%2C%20a%20positive%20integer,28%2C%20496%2C%20and%208%2C128.) from a range entered by a user (include 0).



Coding challenge-⚔️

1) Write a program to display terms of this infinite pattern until 50.
```
1, 2,2,3,3, 4,4,4,5,5,5,6,6,6, 7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,.....
```

Comment your answers below. Let's see who can solve tis one. 🗡️🛡️ Beware, it is harder than it seems....😉

Answer to this question will be given in Day 9. 🤞 So stay tuned by following me for updates 👍. Please like and comment on [dev.to](https://dev.to/aatmaj/learning-python-basic-course-day-7-exercises-and-coding-challenges-2l2b) or fork the repo. 😊

 
