# [Learning Python- Intermediate course: Day 39, OOP-Constructor __init__](https://dev.to/aatmaj/learning-python-intermediate-course-day-38-oop-constructor-init-2lhj)

Originally opublished on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-38-oop-constructor-init-2lhj)

Today let us check out class constructors in Python
---
____
### Constructors in Python
Constructors are class methods which are used to set the class parameters a the time of instantiation. These methods are run automatically when the class is instantiated. 
> The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created. A constructor can optionally accept arguments as well, just like a regular function.

#### Syntax
The constructor is created by the `__init__` keyword.

```python
class sample:
   def  __init__(self):
        print("Class instantiated")
        
mysample=sample()
```
```
Class instantiated
```
___
Forgetting to write the `self ` keyword will geneate error
```python
class sample:
   def  __init__():
        print("Class instantiated")

mysample=sample()

```
```
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    mysample=sample()
TypeError: __init__() takes 0 positional arguments but 1 was given

```
___
The `__init__` method runs once class is instantiated. 
It can be called from outsoide the class too.
```python
class sample:
   def  __init__(self):
        print("Class instantiated")

mysample=sample()
mysample.__init__()
```
```
Class instantiated
Class instantiated
```
___
Moreover, it can be called by other methods inside the class.
Here is example.

```python
class sample:
   def  __init__(self):
        print("Class instantiated")
   def fun(self):
       self.__init__()
       print("inside a function")
mysample=sample()
mysample.fun()
```
```
Class instantiated
Class instantiated
inside a function

```



#### Every class has a constructor
But yesterday, when we created a class, we did not use any constructors right? Then is the above statement false?
No. When we do not specify a constructor in a class, a default constructor is generated automatically. This is called the default constructor. When we write a constructor by our own, the default constructor is not generated.

> **Remember this** When you create a class without a constructor, Python automatically creates a default constructor for you that doesn't do anything. Every class must have a constructor, even if it simply relies on the default constructor.


___
### Destructors in Python.
> The users call Destructor for destroying the object. In Python, developers might not need destructors as much it is needed in the C++ language. This is because Python has a garbage collector whose function is handling memory management automatically. The `__del__()` function is used as the destructor function in Python. The user can call the `__del__()` function when all the references of the object have been deleted, and it becomes garbage collected.

The `__del__` is pretty much similar to `__init__` More about it [here](https://www.studytonight.com/python/destructors-in-python)

___
### Parametrized constructors
We can pass parameters to the constructors which set the values of the class 'variables'

Let us see a modification of yesterday's program now using the `__init__` constructor.

```python
class sample:
   rate=3
   def  __init__(self,amount):
        self.amount=amount
   def calculate_tax(self):
       print(self.rate*self.amount*0.01)
mysample=sample(200)
mysample.calculate_tax()
```
```
6.0
```
___
### Multiple constructors.

> Python does not support explicit multiple constructors, yet there are some ways using which the multiple constructors can be achieved. If multiple `__init__` methods are written for the same class, then the latest one overwrites all the previous constructors

```python
class sample:
   rate=3
   def  __init__(self,amount):
        self.amount=amount
   def __init__(self,amount,rate):
       self.amount=amount
       self.rate=rate
   def calculate_tax(self):
       print(self.rate*self.amount*0.01)
mysample=sample(200)
mysample.calculate_tax()
```
```
Traceback (most recent call last):
  File "main.py", line 13, in <module>
    mysample=sample(200)
TypeError: __init__() missing 1 required positional argument: 'rate'

```

**One way to use multiple constructors is using `*args` But that's not for today....**


> Python natively does not support function overloading - having multiple functions with the same name.

____
So friends that was all for today! Let us understand how inheritance is implemented in Python tomorrow.
