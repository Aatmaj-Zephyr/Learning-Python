[Learning Python-Basic course: Day 18, Dictionaries in Python](https://dev.to/aatmaj/learning-python-basic-course-day-18-dictionaries-in-python-30af)

Original;y published on the dev.to platform [here.](https://dev.to/aatmaj/learning-python-basic-course-day-18-dictionaries-in-python-30af)

## Welcome all🤟 Today we will cover dictionaries!

---

Dictionary is simply a collection of unordered key value pairs
Or sometimes referred as a 'hash table' of key value pairs. Dictionary holds key:value pair. this means that every value in an dictionary is mapped with some other value. Values in a dictionary can be of any datatype. Dictionaries cannot have two items with the same key for obvious reasons.
example

```
AatmajProfileDictionary={"name":"Aatmaj","Hobby":"teaching","Commits":700}
```

Here is a quick difference between lists, tuples and dictionaries.
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/l74vjn5pxz9vixtdxynm.png)

```python
a=[] #list
a=() #tuple
a={}#dictionary
```

### Hash table

A Hash table is a data structure. A hash table is a data structure that implements an associative array abstract data type that can map keys to values. A hash table uses a hash function to compute an index also called as the hash code, into a array of buckets or slots, from which the desired value can be found.

> As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

## Sample program-

Here is a sample program just to get you started with dictionaries. It is quite easy to understand and commented whenever necessary

```python
>>> hardware={    "Brand": "Dell",    "Model": 2430,    "Year":  "2020"}
>>> print(hardware) #prints the value of the dictionary
{'Brand': 'Dell', 'Model': 2430, 'Year': '2020'}
>>> print(hardware["Model"])
2430
>>> print(hardware.get("Model"))
2430
>>> hardware["Year"]=2021 #Changing the value of the dictionary
>>> print(hardware)
{'Brand': 'Dell', 'Model': 2430, 'Year': 2021}
>>> print(hardware.pop("Model"))
2430
>>> print(hardware)
{'Brand': 'Dell', 'Year': 2021}
>>> hardware["Model"]="Lenovo"
>>> hardware["Year"]=2019
>>> print(hardware.popitem()) #popitem returns the last value entered
('Model', 'Lenovo')
>>> print(hardware)
{'Brand': 'Dell', 'Year': 2019}
>>> for y in hardware:
...     print(y)#Corresponds to each key
...
Brand
Year
>>> for x in hardware:
...      print(hardware[x])#refers to the value
...
Dell
2019
>>> for z in hardware.values():
...      print(z)
...
Dell
2019
>>> hardware.clear() #Cleares the dictionary (not delete)
>>> print(hardware)
{}
>>> print(hardware["Price"])#trying to remove element which is not present
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Price'
```

### Multidimensional dictionaries

Same story needs no explanation!

```python
hardware={
    "LAPTOP":{"Brand": "Dell","Model": 2430,"Year":  "2020"},
    "DESKTOP":{"Brand":"Lenovo","Model":8877,"Warranty": 2},
    "TABLET":{"Brand":"Apple", "price":"3000$"}
}
print(hardware)
print(hardware["TABLET"])
print(hardware["LAPTOP"]["Model"]) #Note the syntax
```

```
{'TABLET': {'price': '3000$', 'Brand': 'Apple'}, 'LAPTOP': {'Model': 2430, 'Brand': 'Dell', 'Year': '2020'}, 'DESKTOP': {'Model': 8877, 'Brand': 'Lenovo', 'Warranty': 2}}
{'price': '3000$', 'Brand': 'Apple'}
2430
```

Exercise-

1. Make a dictionary which contains a list and a tuple. Then append the tuple in the list in the dictionary.

2. **Dynamic generation of dictionaries**- Write a program to take names of five students and their corresponding marks, put them in an dictionary.
   output-

```
Please enter student name peter
Please enter marks 13
Please enter student name john
Please enter marks 32
Please enter student name pappu
Please enter marks 5
Please enter student name bob
Please enter marks 7
Please enter student name mina
Please enter marks 32
{'peter': 13, 'john': 32, 'pappu': 5, 'mina': 32, 'bob': 7}
```

Answers will be found [here](https://github.com/Aatmaj-Zephyr/Learning-Python/tree/main/Basic/Day%2018)

So friends that's all for this part. 😊For any suggestions please ping me🤠.
Here is my Gmail- aatmaj.mhatre@gmail.com 🤟
Don't forget to follow me for updates on the course.😊
