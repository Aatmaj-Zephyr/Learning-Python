# [Learning Python-Basic course: Day 21, Summary of the week and dictionary exercises.](https://dev.to/aatmaj/learning-python-basic-course-day-21-summary-of-the-week-and-dictionary-exercises-391e)

Originally published on the Dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-21-summary-of-the-week-and-dictionary-exercises-391e)

## Today we will do more questions related to dictionaries for a thorough revision. In the process, we also will learn a few methods related to dictionaries.

---

Summary of the week-

- [Day 18](https://dev.to/aatmaj/learning-python-basic-course-day-18-dictionaries-in-python-30af) We learnt about dictionaries. We checked out one example which covered many inbuilt functions related to dictionaries.
- [Day 19](https://dev.to/aatmaj/learning-python-basic-course-day-19-practicing-dictionary-exercises-1723) We practiced a few questions on dictionaries and had quite a thorough practice of dictionaries in Python. We did programs to fuse two separate lists to a single dictionary, paired out even numbers and made fancy dictionaries using for loops.
- [Day 20](https://dev.to/aatmaj/learning-python-basic-course-day-20-hashtables-via-dictionaries-3nf1) We learnt about hashtables and how to create them using dictionaries. We tried out simple and chained hashtables and worked out information retrieval using them.

---

## Sample question-Concatenate two dictionaries.

We will now fuse two dictionaries to create a new one using the `update()` method

```python
a={1:10, 2:20}
b={3:30, 4:40}
c={}
for i in (a,b):
    #for every element in dictionary a AND dictionary b,
    c.update(i)
    #update the dictionary to include these values.
print(c)
```

output-

```
{1: 10, 2: 20, 3: 30, 4: 40}
```

**Conflict resolution**- In case both the dictionaries have a same key, in that case the last value is held true by the `update()` method.

```python
a={1:10, 2:20}
b={3:30, 4:40 , 2:60}
c={}
d={}
for i in (a,b):
    c.update(i)
print(c)
for i in (b,a):
    d.update(i)
print(d)
```

```
{1: 10, 2: 60, 3: 30, 4: 40}
{1: 10, 2: 20, 3: 30, 4: 40}
```

## Editing keys.

I know what you all must be thinking. Keys are non-mutable right?
Yes. they are. but here is a cleaver trick

```python
a = {
  "a":1,
  "b":2,
  "c":3,
  "e":4
}
# Replace 'e' by 'd'

a["d"] = a.pop("e")
print(a)
```

```
{'b': 2, 'a': 1, 'c': 3, 'd': 4}
```

---

Today there are no exercises from my side..😃...But wait!😒 I am providing a reference link for taking on a dictionary quiz to clear all your concepts!😋
[Dictionary quiz by PYnative](https://pynative.com/python-dictionary-quiz/)
The quiz contains 14 Questions. 14/14 is the target

Comment your progress below by pasting screenshot of your scores!🤠

---

✌️So friends that's all for now. 😊 Hope you all are having fun.😎 Please let me know in the comment section on [dev.to](https://dev.to/aatmaj/learning-python-basic-course-day-21-summary-of-the-week-and-dictionary-exercises-391e). And don't forget to like the post there if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the comments below or gmail me. 😉

#### Please do follow me on [Github](https://github.com/Aatmaj-Zephyr) and Star this [Learning Python Repository](https://github.com/Aatmaj-Zephyr/Learning-Python) which contains all the material for this course😁

Thank you all👍

> _For those who have not yet made account in Dev.to, you can have a free easy sign-up using your mail or GitHub accounts. I would suggest the budding developers to create your GitHub free account right away. You would require to register sooner or later anyways_
