[Learning Python-Basic course: Day 19, Practicing Dictionary exercises](https://dev.to/aatmaj/learning-python-basic-course-day-19-practicing-dictionary-exercises-1723)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-19-practicing-dictionary-exercises-1723)

Today we are going to solve some questions related to dictionaries. 😄 So in case you have missed yesterday's blog where we have covered dictionaries in depth, [click here.](https://dev.to/aatmaj/learning-python-basic-course-day-18-dictionaries-in-python-30af)
---
____
Just a bit of revision of dictionaries which we covered yesterday.
**Defination**-
> A dictionary is defined as a general-purpose data structure for storing a group of objects. A dictionary is associated with a set of keys and each key has a single associated value.

Dictionaries are used for retrieving a value from a key
In dictionaries, the keys are mapped with specific values. They are somewhat similer to hashtables. we will cover hashtables in tomorrow's part, but today we will first take a closer look at how dictionaries operate by solving some questions related to them.
_____
**Sample program 1**
Let's see how to fuse two separate lists into a key-value pair dictionary.
```python
a=["a","b","c","d"]#list -key
b=(1,2,3,4)#tuple- value

#Method 1
c={} #empty dictionary
for i in range(0,len(a)):
    c[i]=a[i]
print(c)

#Method 2
d=dict(zip(a,b))
print(d)
```
In the above program, we have fused the keys(list a) and the values(tuple b) into a dictionary(c and d ). In the second method, we have used two methods `dict()` and `zip()`. The `dict()` method is used to create a dictionary while the `zip` method is used to zip together two key-value pairs.


**Sample question 2)**
Write code to make this dictionary using for loop-
```
{0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}
```
Solution-
```python
a={}
for i in range(0,10):
    a[i]=2* i 
print(a)
```
**Exercise 1)** Modify the above code to give the following output-
```
{'d': 16, 'c': 9, 'a': 1, 'b': 4}
```
*(Don't mind the order)*

Sample question 3) Write a program for making the dictionary shown below using for loops-
```python
a={
    1: [1, 2, 3, 4, 5],
    2: [2, 3, 4, 5, 6], 
    3: [3, 4, 5, 6, 7],
    4: [4, 5, 6, 7, 8],
    5: [5, 6, 7, 8, 9]
}
```

Solution-
```python
a={}
for i in range(1,6):
    a[i]=[]
    for j in range(i,i+5):
        a[i].append(j)
print(a)
```
OUTPUT-
```
{1: [1, 2, 3, 4, 5], 2: [2, 3, 4, 5, 6], 3: [3, 4, 5, 6, 7], 4: [4, 5, 6, 7, 8], 5: [5, 6, 7, 8, 9]}
```

Exercise 2)- Modify the above program for making the following dictionary-
```python
b={
    1:[1],
    2:[1,2],
    3:[1,2,3],
    4:[1,2,3,4],
    5:[1,2,3,4,5]
}
```
Answers to the above exercise will be found as usual in the [Learning-Python Repository](https://github.com/Aatmaj-Zephyr/Learning-Python)
#### Fun exercise
Can you find the levels of nesting? first one is solved for you. Answer in the comments below!😏
```python
a={[([1,2,3])]:[[{1:2}]]}
#key: List in a tuple in a list value: dictionary in a list in a list.
b={[1,2]:(((1,2,3)))}
c={1:[([(1,2,3)])]
d={[({[1,2]:[(1,2,3)]})]:[((1,2,{2:3}))]}#invalid... Can you find out why?
e=[[(a,b),c]:(d,(a))]
```

✌️So friends that's all for now. 😊 Hope you all are having fun.😎 Please let me know in the comment sectionon dev.to [here](https://dev.to/aatmaj/learning-python-basic-course-day-19-practicing-dictionary-exercises-1723). And don't forget to like the post if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the comments below or gmail me. 😉
Thank you all👍

Follow me on [GitHub](https://github.com/Aatmaj-Zephyr) for updates
