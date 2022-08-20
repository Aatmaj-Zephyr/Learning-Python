# [Learning Python- Intermediate course: Day 6, Math Exercises](https://dev.to/aatmaj/learning-python-intermediate-course-day-6-math-exercises-12ge)

Originally published ion the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-6-math-exercises-12ge)

## In the last part we covered the math module. In this part, we will solve some questions related to it.

---

### Sample questions.

- Write a program to check if a number is an ["Armstrong number"](https://en.wikipedia.org/wiki/Narcissistic_number) or not

```python
def armstrong(x):
    a=str(x) #convert int to string to make it iteratable
    counter=0
    Sum=0
    for i in a:
        counter=counter+1

    for i in a:
        Sum=Sum+pow(int(i),counter)
    if(Sum==x):
        return True
    return False
print(armstrong(153))
print(armstrong(1723))
```

```
True
False
```

#### Alternative

```python
def armstrong(x):
    n = 0
    i=x
    while (i != 0):
        n = n + 1
        i = i // 10
    temp = x
    Sum = 0
    while (temp != 0):
        r = temp % 10
        Sum = Sum + pow(r, n)
        temp = temp // 10
    return (Sum == x) #shorthand for if Sum==x return True else return False
print(armstrong(153))
print(armstrong(1723))
```

```
True
False
```

- Write the function power which returns the number raise to a power without using the math function `pow()`

```python
def power(x, y):
    if (y == 0):
        return 1
    if (y % 2 == 0):
        return power(x, y // 2) * power(x, y // 2)
    return x * power(x, y // 2) * power(x, y // 2)
print(power(2,3))
print(pow(2,3))
```

```
8
8
```

> **Logic** The function power is a function which makes use of recursion in Python. The power is raised using recursive multiplication.

#### Alternative-

```python
def power(a, b):
    temp=a
    for i in range(1,b):
        temp=temp*a
    return temp
print(power(3,4))
print(pow(3,4))
```

```
81
81
```

### Exercise.

Write the following functions without using their predefined math versions.

- `hypot()`
- `sqrt()`
- `asinh()`

Answers in this [Learning Python Repository](https://github.com/Aatmaj-Zephyr/Learning-Python)

---
