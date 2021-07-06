# [Learning Python-Basic course: Day 10, Lists in Python](https://dev.to/aatmaj/learning-python-basic-course-day-10-lists-in-python-1hcb)

Originally published on the dev.to platform [here.](https://dev.to/aatmaj/learning-python-basic-course-day-10-lists-in-python-1hcb)

Welcome!  🤟 This week is for data structures and related exercises in Python . Today we will study the 'list' data structure. 💎
---
___
# List

List is somewhat similar to arrays in Java. The common thing between lists and arrays is indexing part. Both are indexed in the same way. The differences in them arises in the data types. List is collection different data types, while arrays is a collection of same data types. Here is a technical defination- **A list is a data structure in Python that is a mutable or changeable, ordered sequence of 'items'.**- Every element in a list is indexes with umbers. Each element value in a list is called an 'item'. Moreover, a list is ordered, meaning the order of the element matters. There are inbuilt functions in Python which 'change' the list. but more about of that later..

Let us now see how to make a list. We can make a list using square brackets.
```
a=['a','b','1',2]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
```
OUTPUT-
```
a
b
1
2
```
A few things to note is that `'1'`, `'b'` and `'a'` is of the data type character while `2` is of the data type int.list starts with 0. The first element of the list. There is no fourth index. Now if we try to acess the non-existant fourth element, an error will arise.
Example as in this program
```
a=[1,2,3,4]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
```
OUTPUT-
```
1
2
3
4
Traceback (most recent call last):
  File "main.py", line 6, in <module>
    print(a[4])
IndexError: list index out of range
```
We can print multiple values using the slicing operator
```python
a=['a','b','c','1','2'] 
print(a[0:2]) #the : is the slicing
```
OUTPUT-
```
['a', 'b']
```
We can also directly print the entire lost using `print()`
```python
a=['a','b','c','1','2'] 
print(a) 
```
```
['a', 'b', 'c', '1', '2']
```

Length of a list in Python
The length of a list can be calculated using the `len()` function
It returns the number of elements in the list
```python
a=['a','b','c','1','2'] 
print(len(a)) 
```

We can acess the entire list from the for loop 
```Python
a=['a','b','c','1','2'] 
for i in range(0,len(a)):
 print(a[i]) 
```
OUTPUT-
```
a
b
c
1
2
```
**Inbuilt list methods.**
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4qftd198ybhcu4i8k9gw.png)
 
We will learn the methods using the example below
```python
a=['a','b','c','1','2'] 
print(a)
a.append(2) 
#add 2 at the end
a.append('c')
print(a.count('c'))
#here we are asking how many times the character c is in the list.
#so answer must be 2
print(a.count(2)) 
#here we are asking how many times int 2 is in the list
print(a.index('1'))
#returns the index at the first occurrence of the element
b=['z','e']
a.extend(b)
#Adds the entire list to a
print(a)
```
OUTPUT
```
['a', 'b', 'c', '1', '2']
2
1
3
['a', 'b', 'c', '1', '2', 2, 'c', 'z', 'e']
```

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4uuygexli8ausgzlj5ba.png)
```Python
a=['B','t','m','a','N','Bat']
print(a)
a.insert(1,'a')
#insert a at second position
a.insert(len(a)-1,'-')
#insert '-' at the second last position
print(a)
a.remove('Bat')
#remove first occurance of 'Bat'
print(a)
a.pop()
#removes the last value.
#Pop is opposite of append
#pop also returns the last value.
b=a.pop()
print(b)
#We can also give value to pop to remove the element.
print(a)
print(a.pop(3))
print(a)
```
While popping or removing, make sure not to exceed the length of the list.
OUTPUT-
```
['B', 't', 'm', 'a', 'N', 'Bat']
['B', 'a', 't', 'm', 'a', 'N', '-', 'Bat']
['B', 'a', 't', 'm', 'a', 'N', '-']
N
['B', 'a', 't', 'm', 'a']
m
['B', 'a', 't', 'a']
```
____
Dynamic allocation of lists
```python
names=[] #Declaration of the list without value
print(len(names))
num=int(input("Enter number of Names to be stored in a list "))
for i in range(0,num):
    st=input("Enter a name ")
    names.append(st)
print("Values stored in List: ")
for i in range(0,num):
    print(names[i])
```
OUTPUT
```
0
Enter number of Names to be stored in a list 4
Enter a name B
Enter a name a
Enter a name t
Enter a name m
Values stored in List: 
B
a
t
m
```
The reverse method just reverse the order of the list.

Here is another sample. Try to predict the output which it will give before looking at the cmd line output.
```python
names=["Batman", "123", "Bat","163","1723"]
#1
print(names)

print("\n Frequency of 'Bat' in the list\n")
print(names.count("Bat"))

print("\n Index of '163' in the list\n")
print(names.index("163"))

print("Adding A in the list")
names.append("A")
print("No. of values in the list = ", len(names))
print(names)
print("New list as last names")
lastnames=["L","M","N"]
print(lastnames)
print("names.extend(lastnames)")
names.extend(lastnames)
print("New values in the names list")
print(names)
print("Inserting new names O, at index 4 ")
names.insert(4, "O")
print(names)
print("Removing A from the list ")
names.remove("A")
print(names)
print("pop() function removes the last value from the list")
names.pop()
print(names)
#names.remove(2) #error msg
print("pop() accepts index and string as an argument")
names.pop(3)
print(names)
print("Reverse of a string")
names.reverse()
print(names)

```

OUTPUT cmd-
```python
>>> names=["Batman", "123", "Bat","163","1723"]
#1
>>> print(names)
['Batman', 'Bat', '123', '163', '1723']
>>> names.count("Bat")
1
>>> names.index("163")
3
>>> names.append("A")
>>> len(names)
6
>>> print(names)
['Batman', 'Bat', '123', '163', '1723', 'A']
>>> lastnames=["L","M","N"]
>>> names.extend(lastnames)
>>> names
['Batman', 'Bat', '123', '163', '1723', 'A', 'L', 'M', 'N']
>>> names.insert(4, "O")
>>> names
['Batman', 'Bat', '123', '163', 'O', '1723', 'A', 'L', 'M', 'N']
>>> names.remove("A")
>>> names
['Batman', 'Bat', '123', '163', 'O', '1723', 'L', 'M', 'N']
>>> names.pop()
'N'
>>> names
['Batman', 'Bat', '123', '163', 'O', '1723', 'L', 'M']
>>> names.remove(2)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    names.remove(2)
ValueError: list.remove(x): x not in list
>>> names.pop(3)
'163'
>>> names
['Batman', 'Bat', '123', 'O', '1723', 'L', 'M']
>>> names.reverse()
>>> names
['M', 'L', '1723', 'O', '123', 'Bat', 'Batman']

```

Exercise-

Write a program for the following output-
```
Please enter a number 5
Please enter a number 1
Please enter a number 2
Please enter a number 3
Please enter a number 4
Please enter a number 5
Smallest value=  0  Greatest value=  5

```

[Answer here](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/d7d53bb9cf73f8fe549aed3244028df6de2cfcf2/Basic/Day%2010/Exercise%20solutions/Exercise%201.py)
____
So friends that's all for this part.  😊 Hope you all are enjoying.😎 Please let me know in the [comment section on dev.to](https://dev.to/aatmaj/learning-python-basic-course-day-10-lists-in-python-1hcb) if you liked it or not. 🧐 And don't forget to like the post if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the [comments](https://dev.to/aatmaj/learning-python-basic-course-day-10-lists-in-python-1hcb) or Gmail me. 😉
Thank you for being so patient.👍

And don't forget to star this repo and follow me on GitHub!
