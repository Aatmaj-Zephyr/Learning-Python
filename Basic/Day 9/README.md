# [Learning Python-Basic course: Day 9, Summary of the week and exercises.](https://dev.to/aatmaj/learning-python-basic-course-day-9-summary-of-the-week-and-exercises-ji6)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-9-summary-of-the-week-and-exercises-ji6)

## Today, we will look at the whole week's summary and check out some more questions. The solution to the Day 7 coding challenge is also provided.

---

# Summary of the week-

[Day 6](https://dev.to/aatmaj/learning-python-basic-course-day-6-the-while-loop-and-more-questions-k23)- We learnt about the while loop, while-else and solved questions

[Day 7](https://dev.to/aatmaj/learning-python-basic-course-day-7-exercises-and-coding-challenges-2l2b)- We solved some more exciting questions on the for and while loop, and the coding challenge whose solution is presented today.

[Day 8](https://dev.to/aatmaj/learning-python-basic-course-day-8-unicode-in-python-4pdc)- We learnt about Unicode in Python and solved some questions.

---

Sample questions-

1. Password generator. Write a sample program to input a number and output a 6 Unicode-character password. Divide the number by numbers 1-7 and generate characters using the result.

```python
a=int(input("Please enter a 6 digit number "))
for i in range(1,7):
    print(chr(a//i),end="")
```

Output-

```
Please enter a 6 digit number 1293748 
🥞ﲯ꡴繗攒吺
```

You can find the unicode chart [here](https://www.ssec.wisc.edu/~tomw/java/unicode.html)

2. Write code to give the following output-

```
A
ABA
ABCBA
ABCDCBA
```

Answer-

```python
for j in range(1,5):
 for i in range(1,j+1):
    print(chr(i+64),end="")
 for i in range(-j+1,0):
    print(chr(-i+64),end="")
 print()
```

---

Exercise-

1. Write a program to get 5 characters from user, take its Unicode sum and display the corresponding character for Unicode value. [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/74a1987aa31350d964e6caa1193bfbb7ab87598f/Basic/Day%209/Exercise%20solutions/Exercise%201.py)

```
Please enter a character A
Please enter a character A
Please enter a character T
Please enter a character M
Please enter a character A
Please enter a character J
Please enter a character -
Answer is  Ǜ
```

2. Modify the password generator to include only keyboard characters (Unicode 33 to 126)
   OUTPUT-

```
Please enter a 6 digit number 135689
#P@gk0
```

[Answer]()

---

Solution to the coding challenge.

```python
a=1
n=0
while True:
 if(a>=50):
     break
 n=n+1
 for i in range(0,n):
    for j in range(0,n):
        print(a,end=",")
    if(a>=50):
     break
    a=a+1
```

---

✌️So friends that's all for now. 😊 Hope you all are having fun.😎 Please let me know in the [comment section](https://dev.to/aatmaj/learning-python-basic-course-day-9-summary-of-the-week-and-exercises-ji6) on dev.to.And don't forget to like the post if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the comments below or gmail me. 😉
Thank you all👍

> _For those who have not yet made account in Dev.to, you can have a free easy sign-up using your mail or GitHub accounts. I would suggest the budding developers to create your GitHub free account right away. You would require to register sooner or later anyways_

🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥

⭐Star this repo 🤩 and follow me for updates!🙂 👍 💥 🙏🙏🙏
