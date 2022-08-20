# [Learning Python-Basic course: Day 5, Summary of the week and Interview questions](https://dev.to/aatmaj/learning-python-basic-course-day-5-summary-of-the-week-and-interview-questions-37m0)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-5-summary-of-the-week-and-interview-questions-37m0)

## Yo! 🤟 Today is the day five of our course 👋 The agenda for today is solving some fantastic questions based upon our learning this week. 👓

---

**Summary of the week.**

**[Day 1](https://dev.to/aatmaj/learning-python-basic-course-day-1-introduction-and-installation-ee8)**- We learnt what is Python, installed Python and wrote our very first hello world program. We also understood why Python is advantageous to other languages like C and Java.

**[Day 2](https://dev.to/aatmaj/learning-python-basic-course-day-2-statements-comments-and-indentation-5b71)**- We learnt about Python statement types like assignments, expressions, declarations. We learnt how comments are written and the need of indentation. We then solved a few practice programs.

**[Day 3](https://dev.to/aatmaj/learning-python-basic-course-day-3-operators-and-if-elif-else-51cc)**- We covered logical, relational, assignment and arithmetic operators, saw how they work. Then we understood the if-else syntax and solved a few problems on that.

**[Day 4](https://dev.to/aatmaj/learning-python-basic-course-day-4-the-for-loop-40m8)**- We learnt the For Loop in Python, how it differed from C, and solved some questions. (yes I admit they were boring)

---

Today I am gonna give you few exciting questions to solve, and show you a few myself. In the flow we will also learn printing style and code-structure. A few questions from over here are actually from interviews and coding tests. (No exaggeration here)

1)Here is an easy one to begin with. Write a program to give the output like shown below-

```
1
12
123
1234
12345
```

Solution-

```Python
for i in range(0,5):
    for j in range(0,i+1):
        print(j+1,end='')
    print()
```

Explanation-As seen, there are two nested for loops. The second for loop has end variable i+1, where i is the running variable of the first loop.
You must have noticed the end parameter in the print statement. By default, the python's print function ends with a newline. We can modify it by giving an additional parameter to the function using end. We can end the print parameter using any character using it. The last print at the end of the bracket is the representative for the newline.

2. Write a program to check if numbers from 1-100 are prime or not

```python
for a in range(0,100):
    print(a,end="-")
    IsPrime=0
    for i in range (2,a//2):
        if (a%i==0):
           print("The number is composite ")
           IsPrime=1
           break
        if (IsPrime==0):
           print("The number is prime.")
```

As above, the indention must be clear when dealing with large nested blocks

Exercise

1.  _Actual interview question_- Write a program for this output-

```Python
Please enter a character *

Please enter a number 3

*_

*_*_

*_*_*_

*_*_*_

*_*_

*_

```

[Answer here](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/54c7ea60120184d42b5f8fc611f6fb62294f671d/Basic/Day%205/Exercise%20solutions/Exercise%201.py)

2. User enters a character and a number. If the character is a vowel, then the the program's output is as given-

```
Please enter a character o

Please enter a number 4

o

o
oo

o
oo
ooo

o
oo
ooo
oooo
```

[Answer here](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/1a3ae841dd8077a399ca22e23c5ba75be22a7a6a/Basic/Day%205/Exercise%20solutions/Exercise%202.py)

---

_A bit about the course_
I know, I am going a bit slow. May be too slow for some of you. But this is for the benifit of those who are here for the first time. The basic module of this course is made intentionally slow and elaborate. This week was a gentle intro to Python. In the coming weeks, I will cover all the details of the language. For those who already know coding basics, they can just skim through the blog and mull upon the exercises. The exercises provided will strengthen and reinforce the concepts. Moreover they are directly taken or similar to past coding tests from the interview panel...

---

_Epilogue_- We all know that neither me nor you have ever seen each other. Learning in remote environment is a difficult, and teaching is perhaps even more difficult. Teaching is never a one-way process. When a teacher teaches with pattern, he/she expects that the student must respond back. Either with doubts, remarks or nods of approval.
But friends, being remote, we cannot interact with each other. The only way we can connect is through the [comments](https://dev.to/aatmaj/learning-python-basic-course-day-5-summary-of-the-week-and-interview-questions-37m0) on dev.to pplatform. So I urge everyone to comment on the posts. Currently I am in doubt whether you all are understanding me or not. Should I speed up the pace or maybe explain more clearly? I am not getting any feedback from you. Any doubts, discussions, remarks or even a simple hi from you is a great source of motivation for me. So I look forward to your comments below...😊

> _For those who have not yet made account in Dev.to, you can have a free easy sign-up using your mail or GitHub accounts. I would suggest the budding developers to create your GitHub free account right away. You would require to register sooner or later anyways_

Thank you for being so patient.👍

# Please star the repo 🤩
