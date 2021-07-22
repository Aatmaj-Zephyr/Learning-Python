[Learning Python-Basic course: Day 20, HashTables via Dictionaries](https://dev.to/aatmaj/learning-python-basic-course-day-20-hashtables-via-dictionaries-3nf1)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-20-hashtables-via-dictionaries-3nf1)

## Hashtables and information retrieval
The central theme behind hash tables is smart information storage and retrieval. The data must be stored in such a manner that it becomes very easy to search it. 

Suppose we want to store a data of any thousand numbers ranging from one to a million. Using hashtables, we can efficiently store these numbers in a way which makes it easy for searching. This is possible only if we map the values to 'keys' The idea of hash table is to allow different possibilities of keys that might over to be mapped to the same location in an array. This is done with the help of 'hashfunctions' The hash function takes in a value and maps it to a key.


Example we might take the hash function as taking only the last three digits of the number. So, 45367 will go to the position 367, while 3769 will go to 769. In case of two numbers have same set of last three digits, we can use different algorithms to resolve collision. One way to do that is using 'chained hashtables' or linked hash tables. In this, lists are present in the hashtables instead of numeric values, where the values can be appended. The example below will make things more clear.

In case you are not familiar with hashtables, please visit the following references-
 - [Dev.to](https://dev.to/ayabouchiha/hash-table-data-structure-3gla)
- [Geeks For Geeks](https://www.geeksforgeeks.org/hashing-data-structure/)
- [Hacker Earth](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)
- [Youtube](https://www.youtube.com/watch?v=ea8BRGxGmlA)
- [Java point](https://www.javatpoint.com/hash-table)
- [Programitz](https://www.programiz.com/dsa/hash-table)
- [Tutorials Point](https://www.tutorialspoint.com/data_structures_algorithms/hash_data_structure.htm)
- [Wikipedia](https://en.wikipedia.org/wiki/Hash_table#:~:text=In%20computing%2C%20a%20hash%20table,desired%20value%20can%20be%20found.)


If anyone has more references, then please comment below👇

### Simple hashtable
Let us now see how to make a simple hashtable from using a dictionary. The user enters say five values, and we map them to a table of length ten. If the values of the keys overlap, then error message is generated and new value is ignored. This collisionj management will be handled by the next version of hashtable, i.e. linked hashtables.

 For this program, we use a simple hashfunction given be the modulus operator as - `key = value % length `
```python
a={}
for i in range(0,5):
    b=int(input("Please enter an integer "))
    key=b%10 #very simple hash function for length 10
    try:
        int(a[key]) 
        #to check if the element is already present in the position or not.
        print("error-- value occupied!")
    except:
           a[key]=b 
print(a)
```
OUTPUT-
```
Please enter an integer 2
Please enter an integer 43
Please enter an integer 56
Please enter an integer 63
error-- value occupied!
Please enter an integer 78
{8: 78, 2: 2, 3: 43, 6: 56}
```
**Exercise 1)**-Modify the above code to map Unicode characters to the hashtable.

### Linked hashtable.
We now create a linked hashtable, i.e. hashtable of lists. This way, we solve the issue of the keys in the same position. If there are multiple values for the same list, then the values are appended on a list rather than ignoring them. This method is used for fast data retrieval
```python
a={}
for i in range(0,10):
    b=int(input("Please enter a number "))
    key=b%10
    try:#append to original list exists.
     if key not in a[key]:
      a[key].append(b)
    except:#make a new list
        a[key]=[b]
print(a)
```
```
Please enter a number 23
Please enter a number 45
Please enter a number 65
Please enter a number 34
Please enter a number 79
Please enter a number 86
Please enter a number 54
Please enter a number 123
Please enter a number 457
Please enter a number 389
{3: [23, 123], 4: [34, 54], 5: [45, 65], 6: [86], 7: [457], 9: [79, 389]}
``` 
### Retrieving data from the hashtable

We can retrieve the data from the hashtable very efficiently. In the same way as we added the data, we now will remove and display it. 
```
b=int(input("Please enter the value"))
key=b%10
print(a[key].pop(b))
```

Answers as usual in this [learning python repository](https://github.com/Aatmaj-Zephyr/Learning-Python)
____
Hashtables are  one of the many many data structures present. For more information related to data structures and algorithms, please visit this series of blogs-[Data structures blog series by 
Aya Bouchiha on Dev.to](https://dev.to/ayabouchiha/series/13547)

____
✌️So friends that's all for now. 

Follow me on [GitHub](https://github.com/Aatmaj-Zephyr) for updates
