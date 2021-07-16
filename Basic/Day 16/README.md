[Learning Python-Basic course: Day 16, Fractal lists and other questions](https://dev.to/aatmaj/learning-python-basic-course-day-16-fractal-lists-and-other-questions-1ca6)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-16-fractal-lists-and-other-questions-1ca6)

🤟WELCOME 👍 Today let us look at a few miscellaneous questions related to multidimensional list which use try-except😃
---
____
In case you haven't visited [yesterday's](https://dev.to/aatmaj/learning-python-basic-course-day-15-more-about-try-except-1nmj) blog, please do so. We have covered some really good questions based upon try-except

1) **Alphabetical order of letters.**
```python
a=[]
for i in range(0,4):
   try:
    a.append(ord(input("Please enter a character ")))
   except:
    print("Error!")
a=sorted(a)
#The sorted() method sorts the list and returns the sorted list
# This is an inbuilt function to sort the list. You can also use insertion sort.
for i in range(0,len(a)):
    a[i]=chr(a[i])
print(a)
```

Output-
```
Please enter a character a
Please enter a character d
Please enter a character b
Please enter a character h
['a', 'b', 'd', 'h']
```
> Note- The inbuilt sorted() method is so nice, that it will directly sort the values in alphabetical order even if we do not convert them into integers! Try removing the chr() and ord() functions and running the code.

Till now we hadn't handled errors for the input. However in this example, we handle errors for input values, example we can prevent errors f the user inputs more than one character.
Output-
```
Please enter a character 123
Error!
Please enter a character abc
Error!
Please enter a character -2
Error!
Please enter a character 1a
Error!
[]
```
____
2) **Fractal lists.**
We will now try to generate a fractal list. Fractal list is a multi- multidimensional list looks something like this-
`[1, 2, [1, 2], [1, 2, [1, 2]], [1, 2, [1, 2], [1, 2, [1, 2]]]]`
Got the pattern? Basically we must append the list into itself. So now let us try doing so...
```python
a=[1,2]
for i in range(0,3):
    a.append(a)
print(a)
```
Output-
```
[1, 2, [...], [...], [...]]
```
Well, that didn't work. This is because the python syntax doesn't allow us to append to a list like this. We must use a temp variable to store the value.
```python
a=[1,2]
for i in range(0,3):
    temp=a
    a.append(temp)
print(a)
```
Output
```
[1, 2, [...], [...], [...]]
```
Didn't work either! This is because when we assign `temp=a` and append temp,, then we are doing the same thing as before! The solution is using the copy() method.

```python
a=[1,2]
for i in range(0,3):
    temp=a.copy()
    a.append(temp)
print(a)
```
Output-
```
[1, 2, [1, 2], [1, 2, [1, 2]], [1, 2, [1, 2], [1, 2, [1, 2]]]]
```

### Exercise 
1)- Write a program to find the length of the list in the fractal list. [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/6c0c0c9ba4c276a373fa199b57b680bf70403398/Basic/Day%2016/Exercise%20solutions/Exercise%201.py)

2) Write a program to reverse the lists in a list. Example
```
In: [[1,2,3],4,[5,6],[7,[8,9],10],[11,12,13,14],15]
Out: [[3, 2, 1], 4, [6, 5], [10, [8, 9], 7], [14, 13, 12, 11], 15]
```
Hint- use try except pass for non list values.

[Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/a24ed3f5c3f6b47defc0c41f07c252026262b4ae/Basic/Day%2016/Exercise%20solutions/Exercise%202.py)
___
✌️So friends that's all for now. 😊 Hope you all are having fun.😎 Please let me know in the [comment section on dev.to](https://dev.to/aatmaj/learning-python-basic-course-day-16-fractal-lists-and-other-questions-1ca6) 👇. And don't forget to like the post if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the comments below or gmail me. 😉
Thank you all👍
Star the [Learning-Python repo](https://github.com/Aatmaj-Zephyr/Learning-Python) made for this course!😃

🤫psst... follow me on dev.to and GitHub for updates...

