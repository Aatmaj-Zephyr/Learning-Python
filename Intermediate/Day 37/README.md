# [Learning Python- Intermediate course: Day 37, File handling in Python](https://dev.to/aatmaj/learning-python-intermediate-course-day-37-file-handling-in-python-1pih)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-37-file-handling-in-python-1pih)

Today we cover File-handling in Python in a lightning fast speed
---
____
Many times we need to save data into files for long-term usage. Today we will learn how to write data into a file and retrieve it.

### Opening a file
Python has two types of files, text and binary. But we will now learn only about text files, which are quite popular. 

> How will the interpreter know when to end a line? Each line in a file has the EOL terminating character (example comma or newline character) which the interpreter reads and processes a new line.. 

We can open a file into four modes

- "r"  Reading mode
- "w"  Writing mode
- "a"  Appending mode
- "r+" Both reading and writing

If not passed, then Python will assume it to be “ r ” by default. 

**Syntax for opening a file** We can open a file using the syntax 

```python
file = open('myfile.txt', 'r') # Reading mode
file = open('myfile.txt', 'a') # Writing mode
file = open('myfile.txt', 'w') # Appending mode
file = open('myfile.txt', 'r+') # Both reading and writing
```
> Note than the file name is case sensitive. So `myfile.txt` is not equal to `Myfile.txt`

### Reading from a file
First we make a file named....say `myfile.txt` 
```
A Quick brown fox jumps over the lazy dog
Welcome to PYTHON Programming
```

In case the file doesn't exist, we get this error-
```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    file = open("myfile.txt", "r") 
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'

```
We can read the contents of the file using the `file.read()` method

```python
file = open("myfile.txt", "r") 
print (file.read())
```

OUTPUT
```
A Quick brown fox jumps over the lazy dog
Welcome to PYTHON Programming

```

We can also return a specific number of characters by adding parameters to the read method. For example
```python
file = open("myfile.txt", "r") 
print (file.read(7))
```

OUTPUT
```
A Quick
```

The value returned is a string
```python
file = open("myfile.txt", "r") 
print (type(file.read(7)))
```
```
<class 'str'>
```

We can access the file line by line using the for in loop

```python
file = open("myfile.txt", "r") 
for temp in file:
    print (temp)
```
This syntax prints out each element of the file in lines.
```
A Quick brown fox jumps over the lazy dog

Welcome to PYTHON Programming

```

### Writing into a file
When we write into a file, we do not need to create one. If the file in which we want to write doesn't exist, it gets automatically created.
```python
file = open('myfile.txt','w')
file.write("A Quick brown fox jumps over the lazy dog.")
file.write("Welcome to PYTHON Programming")
file.close()
```
OUTPUT (myfile.txt)
```
A Quick brown fox jumps over the lazy dog.Welcome to PYTHON Programming
```

> The close() command terminates all the resources in use and frees the system of this particular program.

If we want the text into two separate lines, we can use the newline `\n` symbol.

```python
file = open('myfile.txt','w')
file.write("A Quick brown fox jumps over the lazy dog.")
file.write("\n")
file.write("Welcome to PYTHON Programming")
file.close()
```

OUTPUT- (myfile.txt)
```
A Quick brown fox jumps over the lazy dog.
Welcome to PYTHON Programming
```

The write method overrides the file each and every time the file is opened function is called. To avoid this, we can use the append mode to add to the file.

```python
file = open('myfile.txt','a')
file.write("A Quick brown fox jumps over the lazy dog.")
file.write("\n")
file.write("Welcome to PYTHON Programming")
file.close()
```

```
A Quick brown fox jumps over the lazy dog.
Welcome to PYTHON ProgrammingA Quick brown fox jumps over the lazy dog.
Welcome to PYTHON Programming
```

____
So friends we have covered file handling today. From next parts onwards we will cover object oriented programming.
