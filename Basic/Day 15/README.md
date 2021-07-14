# [Learning Python-Basic course: Day 15, More about try-except](https://dev.to/aatmaj/learning-python-basic-course-day-15-more-about-try-except-1nmj)

Originlly published on the dev.to pletform [here](https://dev.to/aatmaj/learning-python-basic-course-day-15-more-about-try-except-1nmj).

Today we will do some practice related to the `try`  error handling we learnt yesterday.
---
____

Sample program-

1) **Tuple or List?** Remember we covered basics of tuples on [Day 11](https://dev.to/aatmaj/learning-python-basic-course-day-11-multidimensional-lists-and-tuples-3bfl)? Now we write a program to check if a data type is a List or a Tuple.
```python
a=[1,2,3] #list
b=(1,2,3) #tuple
c=[b,2,4] #list
d=(1,b,c) #tuple
check=[a,b,c,d] 
for i in check:
    try:
        i.append(1)
        print(i," is a List")
    except:
        print(i," is a Tuple")
```
> This example needs strong understanding of Tuples and multidimensional Lists, so in case you are not comfortable with  either of them, please refer to [Day 11](https://dev.to/aatmaj/learning-python-basic-course-day-11-multidimensional-lists-and-tuples-3bfl)

Output-
```
[1, 2, 3, 1]  is a List
(1, 2, 3)  is a Tuple
[(1, 2, 3), 2, 4, 1]  is a List
(1, (1, 2, 3), [(1, 2, 3), 2, 4, 1])  is a Tuple
``` 

The logic behind this code is that when we try operations like pop, append, push etc. on tuples, they generate errors. We exploit this non-mutable property of Tuples to distinguish between the two. If error generated, it is a Tuple else a List.



# Nested `try` `except`

We can generate a nested `try` `except` in a similar manner,  however there is a glitch
```python
try:
    try:
        #statament 1
    except:
        pass
except:
     #statement 2
```

Here, statement 2 won't ever run. Can you think why? 

This is because the first `try` will not give any error. This is because any no error will be given by the nested `try` `except pass`

Here is when we need a nested `try` is useful.

```python
try:
    #statement 1
    try:
        #statament 2
    except:
        #statement 3
except:
     #statement 4
     # executed if error is in statements 1 or 3
```

# Exercise-
Write a program to check if a number if less than, greater than or equal to 15 without using if -else. (hint use `chr()` along with `try` )
[Do-Not-See-This-Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/f50437e11abb103b0f7411beba5da413045d812a/Basic/Day%2015/Exercise%20solutions/Exercise%201.py)

Comment your answers on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-15-more-about-try-except-1nmj). Let's see who can solve this one. 🗡️🛡️ Beware, it is harder than it seems....😉


