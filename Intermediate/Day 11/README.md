# [Learning Python- Intermediate course: Day 11, Random numbers](https://dev.to/aatmaj/learning-python-intermediate-course-day-11-random-numbers-5cnj)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-11-random-numbers-5cnj)

## Today we will cover the random module in Python.

---

Just like the math and cmath modules, the 'random' module is built in into Python, so we do not need to take any extra efforts to download or install it.😊

### Generating a random number

The `random()` method in random module generates a floating point number between 0 and 1. Note that Python is case sensitive, hence `random()` and `Random()` are different!

```python
import random #import the random module
for i in range(0,5):
 n = random.random()
 print(n)
```

```
0.8231210971019169
0.7495851490827552
0.1910088487916375
0.7611387314935155
0.17622975226933524
```

---

But many times we want a number in between a specific range of numbers. This is where the `randint()` method comes handy. The `randint()` method generates a integer between a given range of numbers.

```python
import random
for i in range(0,5):
 n = random.randint(3,7)
 print(n)
```

```
7
4
3
6
7
```

Note that the input parameters of the `randint()` gives must be in ascending order only. For example this won't work

```python
import random
for i in range(0,5):
 n = random.randint(7,5)
 print(n)
```

```
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    n = random.randint(10,7)
  File "/usr/lib/python3.4/random.py", line 218, in randint
    return self.randrange(a, b+1)
  File "/usr/lib/python3.4/random.py", line 196, in randrange
    raise ValueError("empty range for randrange() (%d,%d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (10,8, -2)
```

> The `random()` method is often used in data science and statistical operations to obtain random numbers between 0 to 1. For other applications, in most cases the `randint()` function becomes useful

Typing 'random' every time is just a waste right? We can shorten up the code by replacing random with a short keyword, whoch we can use everytime. The syntax for the following is

`import random as rd`

So now every time instead of writing `random`, we can just write `rd`
Example-

```python
import random as rd
for i in range(0,5):
 n = rd.randint(1,10)
 print(n)
```

```
5
1
2
9
9
```

### List of random numbers.

Many times, we require to have a list of random numbers.

One way to do that is appending random numbers to the list. We first create an empty list and then append the random numbers one by one.

```python
import random as rd
randomlist = []
for i in range(0,5):
 randomlist.append(rd.randint(15,30))
print(randomlist)
```

```
[23, 15, 26, 26, 18]
```

Another way is by using the method `sample()`.

The `sample()` method takes two arguments. One is the list of numbers to choose random numbers from, and the other is the number of random numbers to choose. The examples below will make things clear.

```python
import random as rd
randomlist = rd.sample(range(15, 30), 5)
print(randomlist)
```

```
[28, 24, 15, 26, 19]
```

> The `range()` function returns a list of values from the start to the end.

```python
import random as rd
randomlist = rd.sample([2,3,5,7,11,13,17], 5)
#Here the sample returns a random number from the list of prime numbers provided.
print(randomlist)
```

```
[7, 5, 2, 3, 17]
```

✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

😎 Your suggestions motivate me, so please please please let me know in the [comment section on dev.to](https://dev.to/aatmaj/learning-python-intermediate-course-day-11-random-numbers-5cnj) if you this part or not. 🧐 And don't forget to star this repository if you did😍
