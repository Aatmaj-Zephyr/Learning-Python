# [Learning Python-Basic course: Day 11, Multidimensional lists and Tuples](https://dev.to/aatmaj/learning-python-basic-course-day-11-multidimensional-lists-and-tuples-3bfl)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-11-multidimensional-lists-and-tuples-3bfl)

Welcome! 🤟 Today we will learn Multidimensional lists and Tuples💎
---
____
### Multidimensional lists
Multidimensional lists or fondly called list of lists can be made using the following syntax
```python
list=[[1,2,3],[2,3,4],[3,4,5]]
```
This creates a 3 by 3 list. However, in the memory, the values are stored sequentially.
Let us now see a sample to get things clear
```python
>>> list=[[1,2,3],[2,3,4],[3,4,5]]
>>> print(list[1])
[2, 3, 4]
>>> print(len(list))
3
>>> print(list[2][1])
4
>>> print(len(list[0]))
3
>>> print(list)
[[1, 2, 3], [2, 3, 4], [3, 4, 5]]
>>> for i in range(0,len(list)):
...  for j in range(0,len(list[i])):
...   print(list[i][j])
...
1
2
3
2
3
4
3
4
5
>>> for i in list:
...  for c in i:
...   print(c,end="")
...  print()
...
123
234
345
```
The last statement is the mysterious way python implements it's syntax. Rather than writing in range, we can easily take this shortcut.

We can create multidimensional lists dynamically. Here is a sample showing how to.
```python
a=[]
r=int(input("Please enter the number of rows "))
c=int(input("Please enter the number of columns "))
for i in range(r):
    #Append an empty sublist
    a.append([])
    for j in range(c):
        num=int(input("Enter a value "))
        a[i].append(num)

print(a)
for i in a:
     for j in i:
         print(j, end="\t")
         #here, "\t" stands for tab, i.e. leave spaces
     print()
```

Output-
```
Please enter the number of rows 3
Please enter the number of columns 2
Enter a value 1
Enter a value 2
Enter a value 3
Enter a value 4
Enter a value 5
Enter a value 6
[[1, 2], [3, 4], [5, 6]]
1	2	
3	4	
5	6	
```

___

### Tuples in Python
 Tuples are used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable.

In other words the basic difference between list and tuple is that list is mutable, while tuple is not. No one can't modify tuple later. **Tuple is a predefined (fixed) list.** 
In similar way, we can make tuples of tuples or tuples of lists too!

Here is a sample
```python
>>> a=('Aatmaj','Zephyr',163,'1234')
>>> b=(1,2,3,4,5)
>>> c='a','b','c','d'
>>> print(a)
('Aatmaj', 'Zephyr', 163, '1234')
>>> print(len(a))
4
>>> print(a[3])
1234
>>> d=((1,2,3),a,b,('a','c','2',5))
>>> print(d)
((1, 2, 3), ('Aatmaj', 'Zephyr', 163, '1234'), (1, 2, 3, 4, 5), ('a', 'c', '2', 5))
>>> print(len(d))
4
>>> print(len(d[1]))
4
>>> print(d[2][3])
4
>>> print(d[4][2])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> a.append(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
```

____

Exercise-
Let a be a matrix as shown-
```
   1 2 3
a= 4 5 6 
   7 8 9
```
Write code for the following output-
1) Print a

2) Print the transpose of a-
```
147
258
369
```

3) Print lower diagonal elements of a
```
1
45
789
```
4) Print the top left diagonal
```
123
45
7
```

____
✌️So friends that's all for now. 😊 Hope you all are having fun.😎 Please let me know in the [comment section on dev.to](https://dev.to/aatmaj/learning-python-basic-course-day-11-multidimensional-lists-and-tuples-3bfl). And don't forget to like the post on dev.to if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the comments or gmail me. 😉
Thank you all👍

Please follow me on Github and star the repo😊

