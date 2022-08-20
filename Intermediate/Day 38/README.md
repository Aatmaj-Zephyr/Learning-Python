# [Learning Python- Intermediate course: Day 38, OOP](https://dev.to/aatmaj/learning-python-intermediate-course-day-38-oop-197)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-38-oop-197)

## Today we will learn about OOP in Python. Today we will make a simple class and use instances of the classes.

---

Almost everything in Python is an Object, with its properties and methods. A class is like an object blueprint for creating objects. To create a class, use the keyword class:

Here is an example of a sample class commented wherever required

```python
class sample: # creating a class named sample

    # ATTRIBUTES
    x=5 # class data has variable  named x with value five.

# OBJECT CREATION(INSTANTIAZATION OF AN OBJECT)
mysample=sample() # creating an instance of the class

#Accessing the parameters
print(mysample.x) # We can access the attribute values using the '.' operator.
```

```
5
```

Let us see one more sample

```python
class sample:
    number=20
    character='3'

a=sample()
print(a.number+int(a.character))

```

```
23
```

### Class methods

We can put functions inside a class, which are called as 'methods'
Syntax

```
def functionname (classname,......arguments......):
 ...
 ...
 ...
```

The below example will make things very clear

```python
class sample:
    name="Tom"
    number=20
    character='3'
    def printname(sample):
        print(sample.name)

a=sample()
a.printname()
```

```
Tom
```

In the method, one of the arguments passed was the class itself. This is necessary syntax in Python. If it is not done in the same manner, the program won't run. Below are code snippets of how a program won't run.

**Common mistakes**

1. Didnt use the dot operator in the method syntax

```python
class sample:
    name="Tom"
    number=20
    character='3'
    def printname(sample):
        print(name)

a=sample()
a.printname()
```

```
Traceback (most recent call last):
  File "main.py", line 9, in <module>
    a.printname()
  File "main.py", line 6, in printname
    print(name)
NameError: name 'name' is not defined
```

2. Forgot to mention the classname in the arguments

```python
class sample:
    name="Tom"
    number=20
    character='3'
    def printname():
        print(name)

a=sample()
a.printname()
```

```
Traceback (most recent call last):
  File "main.py", line 9, in <module>
    a.printname()
TypeError: printname() takes 0 positional arguments but 1 was given

```

---

###### Tired of writing the name of the class every time? Well use the `self` keyword

The `self` keyword can be used in place of the entire class name

```python
class sample:
    name="Tom"
    number=20
    character='3'
    def printname(self):
        print(sample.name)

a=sample()
a.printname()
```

```
Tom
```

Even replacing the class name by self **inside** the method works

```python
class sample:
    name="Tom"
    number=20
    character='3'
    def printname(self):
        print(self.name)

a=sample()
a.printname()
```

```
Tom
```

### Returning values

We can make the methods return value as we would do in the usual methods

```python
class sample:
    name="Tom"
    number=20
    character='3'
    def printname(self):
        return (self.name)

a=sample()
print(a.printname())
```

```
Tom
```

Let us take one more example related to the methods.

```python
class sample:
    rate=15

    def set_amount(self,amount):
        sample.amount=amount
    def print_tax(self,amount):
        self.set_amount(amount)
        # Exercise why not self.set_amount(self,amount) ?
        print(self.rate*self.amount/100)


a=sample()
a.print_tax(20)
```

```
3.0
```

Here, `set_amount(self)` is a setter method, i.e. This methods sets the values of the method object.

### Exercise

1. What will happen if we replace `self.set_amount(amount) ` by `self.set_amount(self,amount) `?
2. Write a program which contains a class student which contains variables Id, name and roll number
   The class must have methods `showId` and `showrollnumber()`

### Private methods

We will now see how to make class methods as private. The private methods can only be accessed from **inside** the class. No one outside can access it.
In the above example, the `set_amount` is used only inside the class. So why not mark it private? We can set private methods in Python by adding two underscores to the class name, like this `__set_amount` Rest all remains the same

```python
class sample:
    rate=15

    def __set_amount(self,amount):
        sample.amount=amount
    def print_tax(self,amount):
        self.__set_amount(amount)
        print(self.rate*self.amount/100)


a=sample()
a.print_tax(20)
```

```
3.0
```

This private method can not be accessed outside of the class

```python
class sample:
    rate=15

    def __set_amount(self,amount):
        sample.amount=amount
    def print_tax(self,amount):
        self.__set_amount(amount)
        print(self.rate*self.amount/100)


a=sample()
a.__set_amount(2)
a.print_tax(20)
```

```
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    a.__set_amount(2)
AttributeError: 'sample' object has no attribute '__set_amount'

```

---

So friends that was all for this part. In the next part we will study the `__init__` or the class constructor.

Thank you
