[Learning Python-Basic course: Day 17, Summary of the week and Insertion sort](https://dev.to/aatmaj/learning-python-basic-course-day-17-summary-of-the-week-and-insertion-sort-4bi0)

Originallly published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-17-summary-of-the-week-and-insertion-sort-4bi0)

# 🤟Today we will learn about the insertion sort code, then write a program to change capital and small cases.
---
____
## Summary of the week
- [Day 14](https://dev.to/aatmaj/learning-python-basic-course-day-14-basic-exception-and-error-handling-using-try-except-5f38)- we covered the `try` `catch` statements, and basic exception handling. Advanced exception handling and types of exceptions, user defined exceptions is for later.
- [Day 15](https://dev.to/aatmaj/learning-python-basic-course-day-15-more-about-try-except-1nmj)- We solved some creative questions based on `try` `catch` and learnt about nesting them. We also saw one really challenging question related to `try` `except` [here](https://dev.to/aatmaj/learning-python-basic-course-day-15-more-about-try-except-1nmj).
- [Day 16](https://dev.to/aatmaj/learning-python-basic-course-day-16-fractal-lists-and-other-questions-1ca6) We solved more questions on lists now with the added power of `try` `except`. We covered questions like fractal lists, alphabetical order of lists and reversing lists.

## Insertion sort.
Insertion sort is a simple sorting algorithm. It works similar to the way you sort cards. If you are new to this algorithm, check out [this link](https://www.geeksforgeeks.org/insertion-sort/).

```python
a=[1,4,3,5,2]
for i in range(1, len(a)):
    #key = a[i]
    for j in range(0,i):
        if(a[j]<a[i]):
            (a[j],a[i])=(a[i],a[j])#swap
print(a)
'''
Logic-
Set the key equal to the first unsorted value.
Compare the key and the sorted elements.
Move the key to the required position.
'''
```
Output-
```
[5, 4, 3, 2, 1]
```

The code enclosed in block comments  `'''` is block comments. Whenever working in teams, such documentation is of critical. More about it [here](https://dev.to/aatmaj/document-today-or-repent-tommorrow-1mg8).
> For those who are new to Data structures and algorithms, please check out this course on dev.to.-[Data structure & algorithms Series' Articles](https://dev.to/ayabouchiha/series/13547)



**Exercise**

 We did the alphabetical ordering yesterday(In case you missed it- [here](https://dev.to/aatmaj/learning-python-basic-course-day-16-fractal-lists-and-other-questions-1ca6)) Replace the sorted() method used in it with insertion sort. [Answer here](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/81fab3a1d869f4d75a0caecae1cf2abfbaff31f6/Basic/Day%2017/Exercise%20solutions/Exercise%201.py)

___
Sample question
1) **Capital to Small** Write a program to turn capital letters into small case and small case to  capital case in a list.
```python
a=[]
for i in range(0,4):
    a.append(ord(input("Please enter a letter ")))
for i in range (0,len(a)):
 if(65<=a[i]<=65+26): #65=A
    print(chr(a[i]-65+97))
    #65=A, 97=a 
 elif(97<=a[i]<=97+26): #65=A
    print(chr(a[i]+65-97))
 else:
    print("Error. Please enter only characters.")
```
Output-
```
Please enter a letter a
Please enter a letter B
Please enter a letter c
Please enter a letter D
A
b
C
d
```
This is an example of error handling using `if-else` statements.

_____
____

✌️So friends that's all for now. 😊 Hope you all are having fun.😎 Please let me know in the [comment section on dev.to](https://dev.to/aatmaj/learning-python-basic-course-day-17-summary-of-the-week-and-insertion-sort-4bi0). And don't forget to like the post if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the comments below or gmail me. 😉
Thank you all👍
___
One more way to ask any doubts is by forking the [repo here](https://github.com/Aatmaj-Zephyr/Learning-Python/tree/main/Basic/Doubts) and sending Pull request of your doubt.
____
> *For those who have not yet made account in Dev.to, you can have a free easy sign-up using your mail or GitHub accounts. I would suggest the budding developers to create your GitHub free account right away. You would require to register sooner or later anyways*

🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
Next day will begin from Tuesday📅, Monday is reserved for.... [MATLAB MONDAYS💥](https://dev.to/aatmaj/launching-matlab-mondays-a-crash-course-nb1) 

### Follow me for updates on [Github](https://github.com/Aatmaj-Zephyr).
