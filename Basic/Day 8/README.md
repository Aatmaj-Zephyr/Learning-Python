# [Learning Python-Basic course: Day 8, Unicode in Python](https://dev.to/aatmaj/learning-python-basic-course-day-8-unicode-in-python-4pdc)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-8-unicode-in-python-4pdc)

🤟 Welcome! Till now, we have dealt enough with numbers. Now is the time to add Unicode to our arsenal.😎
---
____
**Unicode in Python**
####
Python and Java support Unicode characters.😃 The `ord()` method converts a character into its Unicode code. It takes one argument: a string containing a single Unicode character. In other words, given string of length 1, the function returns an integer giving it's corresponding Unicode value. For example, `ord('a')` returns the integer 97, `ord('€')` (Euro sign) returns 8364.
Here is a sample which takes 10 characters and prints their Unicode values-
```python
for i in range(-5,5):#same as (0,10)
 a=input("Please enter any character ")
 print(ord(a))
```
Here is a output-
```
Please enter any character Z
90
Please enter any character e
101
Please enter any character p
112
Please enter any character h
104
Please enter any character y
121
Please enter any character r
114
Please enter any character 1
49
Please enter any character 2
50
Please enter any character #
35
Please enter any character $
36
```
Try it out with your names too!!!

____
The `chr()` function does just the opposite as the `ord()` function. It converts integers into Unicode characters. Example if we input 97, the output will be 'a', and `chr(€)=8364`

Here is a sample program print Unicode characters-

```python
for i in range(0,4):
 n1=int(input("Please enter lower limit "))
 n2=int(input("Please enter upper limit "))
 for i in range(n1,n2):
  print(i," ",chr(i))
```
Now let us input some values. OUTPUT-
```
Please enter lower limit 33
Please enter upper limit 37
33   !
34   "
35   #
36   $
Please enter lower limit 57
Please enter upper limit 62
57   9
58   :
59   ;
60   <
61   =
Please enter lower limit 85
Please enter upper limit 89
85   U
86   V
87   W
88   X
Please enter lower limit 97
Please enter upper limit 103
97   a
98   b
99   c
100   d
101   e
102   f
```

Here is another sample to prove that `ord()` and `chr()` are absolutely opposite of each other
```python
Istrue=True
#Istrue is a boolean value with value default True
for i in range(1,1000):
 a=chr(i)
 if(i!=ord(a)):
     Istrue=False
print(Istrue)
```
```
True
```
Exercise 1) If we interchange `ord()` and `chr()`, will the program still work? [Answer: NO] (https://github.com/Aatmaj-Zephyr/Learning-Python/blob/e3b422f89dca0694d7376aebc2a222675515f4c5/Basic/Day%208/Exercise%20solutions/Exercise%201.md)

2) Write a program to give the following output-

```
Please enter any capital letter G
A B C D E F G 
A B C D E F G 
A B C D E F G 
A B C D E F G 
A B C D E F G 
A B C D E F G 
A B C D E F G 
```
[Answer here.](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/66648cf59324f2510524ca855e06084df6484bf0/Basic/Day%208/Exercise%20solutions/Exercise%202.py)

3) Modify the above program slightly to give the following output.

```
Please enter any capital letter G
A 
A B 
A B C 
A B C D 
A B C D E 
A B C D E F 
A B C D E F G 
```
[Answer here.](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/6e4ee4362ba48198d34ef068da0b9105dfb55c93/Basic/Day%208/Exercise%20solutions/Exercise%203.py)

4) Modify the above program to give the following output-
```
Please enter any capital letter K
A 
B A 
C B A 
D C B A 
E D C B A 
F E D C B A 
G F E D C B A 
H G F E D C B A 
I H G F E D C B A 
J I H G F E D C B A 
K J I H G F E D C B A 
```
[Answer here.](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/d081c79ed7bcb1393777e367c944524054233621/Basic/Day%208/Exercise%20solutions/Exercise%204.py)

The programs may look repetitive, but trust me, they provide a good practice for practicing nested for loops.
____
✌️So friends that's all for now. 😊 Hope you all are having fun.😎 Please let me know in the [comment section](*https://dev.to/aatmaj/learning-python-basic-course-day-8-unicode-in-python-4pdc) on dev.to 👇. And don't forget to like the post if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the comments below or gmail me. 😉
Thank you all👍

⭐Star this repo 🤩 and follow me for updates!🙂 👍 💥 🙏🙏🙏

