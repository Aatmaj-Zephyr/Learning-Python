# [Learning Python- Intermediate course: Day 44, Summary of the week, examples and exercises](https://dev.to/aatmaj/learning-python-intermediate-course-day-44-summary-of-the-week-examples-and-exercises-3lfg)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-44-summary-of-the-week-examples-and-exercises-3lfg)

## Today we will have a quick summary of the week

---

Let us see a sample OOP program

```python
class animal:
 food=""
 def makenoise(Self):
     pass

class pet():
    def bepetted(self):
        print("Pet me")

class canine():
    def shownails(self):
        print("My nails are long")

class dog(pet):
    def __init__(self):
        print("I am a dog")
        self.food="bone"
    def makenoise(self):
        print("Woof!")

class cat(pet,canine):
    def __init__(self):
        self.food="milk"
        print("I am a cat")
    def makenoise(self):
        print("meow!")

Tommy=dog()
Tommy.makenoise()
Tommy.bepetted()
print(Tommy.food)
Dina=cat()
Dina.shownails()
Dina.bepetted()
print(Dina.food)
```

```
I am a dog
Woof!
Pet me
bone
I am a cat
My nails are long
Pet me
milk
```

---

### Exercises-

#### 1) Correct the following code

```python
class sample():
 def fun(self):
  print("yo!")

mysample=sample()
sample.fun()
```

```
Traceback (most recent call last):
  File "main.py", line 6, in <module>
    sample.fun()
TypeError: fun() missing 1 required positional argument: 'self'
```

#### 2) Correct the following code

```python
class sample():
 def fun():
  print("yo!")

mysample=sample()
mysample.fun()
```

```
Traceback (most recent call last):
  File "main.py", line 6, in <module>
    mysample.fun()
TypeError: fun() takes 0 positional arguments but 1 was given
```

#### 3) Extend the above program to include a class tiger and class wild. Add attribute habitat to wild and pet. Use iterable for in loop to call out the methods (hint use try except)

---

### [Day 41](https://dev.to/aatmaj/learning-python-intermediate-course-day-41-inheritance-in-python-53la)

We learnt about inheritance in Python
Inheritance is an OOP concept which provides flexibility and code reusability to the program. We can make changes to the program without altering much code. We can also extend the code by adding new functionality without much effort. Inheritance in Python is achieved by adding the name of the super classes inside the constructor of the new class. In this part we studied how functions and properties are inherited from the super class. But object constructors are not inherited by the subclasses, however the number of arguments for constructors must be the same for both if the classes. Functions are overloaded in the subclasses, that is the functions with same name can be present in both the subclass and the super class. In such cases, the functions of the sub-class are considered as effective. Constructors and methods of the superclass can be called by the `super()` method in case of overloading.

### [Day 42](https://dev.to/aatmaj/learning-python-intermediate-course-day-42-polymorphism-a61)

In this part we learnt about polymorphism, yet another OOP feature. Just like inheritance, polymorphism too does help in making the program more extendable and flexible. Using polymorphism, we can create new subclasses without doing much change into the superclass. Polymorphism is a technique by which subclasses can be considered as types of super-classes. Polymorphism in Python is achieved through overwriting of methods.

### [Day 43](https://dev.to/aatmaj/learning-python-intermediate-course-day-43-ddd-and-more-on-oop-2npf)

In this part we covered some more of OOP. We covered concepts which are not directly supported by Python, like abstraction and interfaces. We saw a brief about duck typing and how to resolve the Deadly Diamond of Death. This part was just intended to bring together a feeling of completeness regarding OOP concepts and not a complete guide towards OOP.

---

## Intermediate part of the course ends today.

---

So friends, this marks the end of the Learning Python intermediate course. I will be soon providing you all with the summary of the intermediate course.
