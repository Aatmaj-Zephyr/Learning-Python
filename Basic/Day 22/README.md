# [Learning Python-Basic course: Day 22, String Methods Part-1](https://dev.to/aatmaj/learning-python-basic-course-day-22-string-methods-part-1-9j8)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-22-string-methods-part-1-9j8)

Today we will learn about string functions
---
____
Till now, we were using strings for various programs. We used them both as input and output parameters. But now we will learn how to modify them.
This week, we will do operations like break a sentence into words, break strings into letters, capitalize them without using the `ord()` hack or count number of vowels in a sentence.

## String as a list

In Python, we can easily interpret a string as a list of characters. In the example below, we can apply the `len()` function to the string txt, or iterate the for loop. 
But we cannot treat it as a list and do opertions like pop or append()
```python
#Interpreting the string as an array of characters.
txt= "Python"
print(txt)
print("Length of the txt = ", len(txt))

#display string using in keyword
for ch in txt:
    print(ch)


#display the string in original form using range()
for ch in range(0, len(txt)):
    print(txt[ch], end=" ")

print()
#to display in reverse order
for ch in range(len(txt)-1, -1 , -1):
    print(txt[ch], end="")

#We cannot append a character or pop using the standered length functions.
txt.append("a")
print(txt)
```
OUTPUT-
```
Python
Length of the txt =  6
P
y
t
h
o
n
P y t h o n 
nohtyPTraceback (most recent call last):
  File "C:/Users/aatma/Downloads/Example 1 .py", line 21, in <module>
    txt.append("a")
AttributeError: 'str' object has no attribute 'append'
```

## Case changing
We will now see how to handel upper and small cases in Python without any direct use of UNICODE characters.
```python
#1. Upper case the first letter in this sentence:
txt = "hello, AND Welcome"
x = txt.capitalize()
print (x)
#output : Hello, and welcome

#2. Make the string lower case:
txt = "Hello, And Welcome!@#$"
x = txt.lower()
print (x)
#output : hello, and welcome

#3. Make the string upper case:
txt = "Hello, And Welcome"
x = txt.upper()
print (x)
#output : HELLO, AND WELCOME
```
OUTPUT-
```
Hello, and welcome
hello, and welcome!@#$
HELLO, AND WELCOME
```

## Word specific methods
Now let's have a look at more string functions via a program. Comments are there whenever necessary.
```python

#1.Print the word "computer", taking up the space of 25 characters,
#with "computer" in the middle:
txt = "computer"
x = txt.center(25)  

print ("hello",x,"world")
# 2 default spaces+25 total characters. so distance between hello and world must be 27 characters.

#2. Return the number of times the value "act" appears in the string:
txt = "I love programming, programming is my favorite activity"
print(txt)
x = txt.count('i') 

print ("Frequency of the value =" , x)
#case matters. Capital I and small i are treated differently.

#3. Check if the string ends with a punctuation sign .
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

       
#4. Set the tab size to 5 whitespaces:
print("First\tsecond")
txt1 = "ACADEMY"              

txt = "A\tC\tA\tDE\tM Y" # backslah t (i.e. \t) represents tab space. 
x =  txt.expandtabs(6) #expands the tab spaces
print(x)


#5. Locates the word "welcome" in the string and returns the index:
txt = "Hello, welcome to my world."
print(txt)
x = txt.find("welcome")
print(x)
#output : 7
#if the result is -1, string does not exist in the sentence


```
OUTPUT-
```
hello          computer         world
I love programming, programming is my favorite activity
Frequency of the value = 6
True
First	second
A     C     A     DE    M Y
Hello, welcome to my world.
7
```

## Exercises
1)- Write a program to change the capitalization of a user input string and add full stop at the end if it isn't present.
```
Please enter a string: a QUick Brown FOX jumps OVer the Lazy doG
A quick brown fox jumps over the lazy dog.
``` 

2)- Write a program to give the following output-
```
Please enter a string: Python
P 
P y 
P y t 
P y t h 
P y t h o 
P y t h o n 
```

