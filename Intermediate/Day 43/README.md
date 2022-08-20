# [Learning Python- Intermediate course: Day 43, DDD and more on OOP](https://dev.to/aatmaj/learning-python-intermediate-course-day-43-ddd-and-more-on-oop-2npf)

Originally published on the dev.to ploatform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-43-ddd-and-more-on-oop-2npf)

## Today we will cover some OOP properties that are not covered in Python and look at how Python resolves the Deadly Diamond of Death.

---

Python is a language mainly designed to use for data oriented analysis. Today, the most popular use of Python is Data science and ML. Although Python is used as a full-stack to some extent, heavy backending applications which require OOP are still made in Java to a certain extent.

Java is OOP. It is the best suited for design patterns and other beautiful OOP stuff. Python is suited for Data science.. This is why probably Python doesn't support a few features of OOP which are critical to design patterns. Two most significant features are **Abstract classes** and **interfaces**

Although these features may not be available in core Python, we can still use them with the aid of a module know as `abc` But that is not for this course.

> Disclaimer! Advanced concepts like Multiple inheritance, duck typing, abc module will be covered in the advanced part of this course. This part is only for a brief upon those concepts.

---

### Interfaces

Why do we even need interfaces when Python supports multiple inheritance? An interface is the Java workaround for multiple inheritance. All features of interfaces are covered by two python aspects- multiple inheritance and duck typing.

> Still, a few use cases of interfaces are not resolved fully. If you want to make base classes that cannot be instantiated, but provide a specific interface or part of an implementation, interfaces are a must.

#### Duck typing in Python

> "If it walks like duck, swims like duck, looks like a duck, then it probably should be a duck."

In other words, of a class has methods, properties of another class, it is another class. This simply means types go for a toss in Python as long as methods and attributes are the same.

_I know you have not understood anything.... this will be covered in detail in the advanced part of this course._

#### Multiple inheritance in Python

Python supports multiple inheritance. This means that one class can inherit two or more classes. The method resolution is done clearly in Python, unlike C++ and helps resolve most of the issues
More about it in the advanced part of this course

#### Deadly Diamond of Death

Python has a simple way of handling the diamond problem. The method of the first superclass passed is called.

Let us continue with yesterday's program

```python
class ape():
    food=""
    def __init__(self,weight):
        self.weight=weight
    def cry(self):
        pass # Do nothing
    def eat(self):
        print(self.food)

class chimpanzee(ape):
    def __init__(self,weight):
        super().__init__(weight)
        self.food="bananas"
    def cry(self):
        print("I am a chimp")

class gorrilla(ape):
    def __init__(self,weight):
        super().__init__(weight)
        self.food="fruits"
    def cry(self):
        print("I am a gorrilla")

class gorranzee(chimpanzee,gorrilla):
    pass

A=gorranzee(20)
print(A.food)
A.cry()
```

```
bananas
I am a chimp

```

```python
class ape():
    food=""
    def __init__(self,weight):
        self.weight=weight
    def cry(self):
        pass # Do nothing
    def eat(self):
        print(self.food)

class chimpanzee(ape):
    def __init__(self,weight):
        super().__init__(weight)
        self.food="bananas"
    def cry(self):
        print("I am a chimp")

class gorrilla(ape):
    def __init__(self,weight):
        super().__init__(weight)
        self.food="fruits"
    def cry(self):
        print("I am a gorrilla")

class gorranzee(gorrilla,chimpanzee):
    pass

A=gorranzee(20)
print(A.food)
A.cry()


```

```
fruits
I am a gorrilla

```

If gorilla is passed first, then the `cry()` method and constructor of gorilla class will run. And if chimpanzee is passed first, then the cry and constructor of chimpanzee class will be run.

#### Abstract classes

In the above example, ape was the class which needn't be instantiated, and could have been made an abstract class. But Python doesn't support abstract classes in an built way. However, modules can be used to implement abstractions.

### abc module

The abc (Abstract Base Classes) is a inbuilt Python module which enables the usage of abstract classes and inheritance in Python.
This module provides the metaclass ABCMeta for defining ABCs and a helper class ABC to alternatively define ABCs through inheritance.

> The package zope.interface provides an implementation of “object interfaces” for Python. It is maintained by the Zope Toolkit project. The package exports two objects, ‘Interface’ and ‘Attribute’ directly. It also exports several helper methods. It aims to provide stricter semantics and better error messages than Python’s built-in abc module.

[The Twisted Plugin System](https://twistedmatrix.com/documents/current/core/howto/plugin.html) is an alternative to the zope interface.

---

And at last, before ending today's last session, some philosophical sermon

> Python follows the EAFP (Easier to Ask Forgiveness than Permission) rather than the LBLY (Look Before You Leap) philosophy. The EAFP is somewhat linked to the "duck typing" style.
