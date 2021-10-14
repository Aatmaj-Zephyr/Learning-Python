#  [Learning Python- Intermediate course: Day 41, Inheritance in Python](https://dev.to/aatmaj/learning-python-intermediate-course-day-41-inheritance-in-python-53la)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-41-inheritance-in-python-53la)

Today we will learn about inheritance in Python
---
____

### Inheritance
Inheritance provides **Code Reusability**. We do not need to write the same piece of code again and again for various subclasses. This increases **Flexibility** of the code. This means that subclasses can be formed without altering the original classes.

**The inherited class can use functions and variables of the derived class**

### Syntax.
Classes can be inherited by passing the name of the superclass to the brackets `class inherited(master)`

Let us see an example below to demonstrate inheritance in pyuthon

```python
class sample():
 a=2
 b=3
 def fun(self):
     print("Hello world")
     
class sample2(sample):
    def fun2(self):
        print(self.a+self.b)
        
mysample2=sample2()
mysample2.fun()
mysample2.fun2()
```
```
Hello world
5

```

#### Explaination
Here, sample() is the masterclass and sasmple2 is the derived class. The derived class sample2 inherits the master class as we pas the  name of the master class into the derived class bracket.
- `class sample2():` This syntax will create class `sample2`
- `class sample2(sample)`: This syntax will create a class `sample2` and make it inherit the class `sample`

Once the class `sample2` inherits `sample`, it can use it's attributes (like here a and b) in it's body. This is why no errors were generated when we used to variables a and b directly in the function `fun2`. The values fir a and b were assigned in  the master class (`sample2` itself ands need not be assigned again . This is an example of **code reuse** and **information hiding**

The derived class `sample2` can also use the functions declared in the master class. This is how the function `fun` could be used  and run successfully.


I hope you do not have any more doubts, if you have, please feel free to post them in the comments on [Dev.to here](https://dev.to/aatmaj/learning-python-intermediate-course-day-41-inheritance-in-python-53la)


____
### Inheritance of constructors.

**Constructors are not inherited by default.** The example below will make things very clear

```python
class sample():
 a=2
 b=3
 def __init__(self):
     self.a=100
     self.b=50
 def fun(self):
     print("Hello world")
     
class sample2(sample):
    def fun2(self):
        print(self.a+self.b)
        
mysample2=sample2()
mysample2.fun()
mysample2.fun2()
```
```
Hello world
5
```
In the above example, you would expect the output to be 150 and not 5. But it is not so. This is because of the fact the constructors of the master class are not inherited by the derived classes by default. This means that `sample2.__init__` is not the same as `sample.__init__`.

Why? Well remember In the previous parts we learnt that if we do not provide a constructor to the class, Python provides one default constructor automatically? Something similar happened in this case. We did not provide any constructor to the `sample2` class. So python made a default blank constructor in it's place, which had no relation to the master class. 

If we want to add the constructor, we can use the following syntax-

```python
class sample():
 a=2
 b=3
 def __init__(self):
     self.a=100
     self.b=50
 def fun(self):
     print("Hello world")
     
class sample2(sample):
    def __init__(self):
     super().__init__()
    def fun2(self):
        print(self.a+self.b)
        
mysample2=sample2()
mysample2.fun()
mysample2.fun2()
```

Using the super keyword, we can manage the constructors.

Note, even though constructors are not inherited, the arguments of the constructors in both the classes must match. Example shown below

```python
class sample():
 a=2
 b=3
 def __init__(self,var):
     self.a=100
     self.b=50
 def fun(self):
     print("Hello world")

class sample2(sample):
    def fun2(self):
        print(self.a+self.b)

mysample2=sample2()
mysample2.fun()
mysample2.fun2()
```
```
Traceback (most recent call last):
  File "main.py", line 14, in <module>
    mysample2=sample2()
TypeError: __init__() missing 1 required positional argument: 'var'
```
...
```python
class sample():
 a=2
 b=3
 def __init__(self,var):
     self.a=100
     self.b=50
 def fun(self):
     print("Hello world")

class sample2(sample):
    def fun2(self):
        print(self.a+self.b)

mysample2=sample2(3)
mysample2.fun()
mysample2.fun2()
```
```
Hello world
150

```
____
**Exercise** What is the output of the following program? and why?
```python
class sample():
 a=2
 b=3
 def __init__(self):
     self.a=100
     self.b=50
 def fun(self):
     print("Hello world")
     
class sample2(sample):
    def __init__(self):
     a=100
     b=200
    def fun2(self):
        print(self.a+self.b)
        
mysample2=sample2()
mysample2.fun()
mysample2.fun2()
```

Solution-
The output is
```
Hello world
5

```
This is because `self.a=100` and `self.b=200` should haver been written in place of `a=100` and `b=200`


____
Function overloading in Python
What if two functions have the same name in the master class as well as the derived class? Well the answer is simple the function in the derived class will be considered. 
This is know as function overloading.

```python
class sample():
 a=2
 b=3
 def __init__(self):
     self.a=100
     self.b=50
 def fun(self):
     print("Hello world")
     
     
class sample2(sample):
    def __init__(self):
     super().__init__()
    def fun(self):
        print(self.a+self.b)
        
mysample2=sample2()
mysample2.fun()

```
```
150
```

If we want to use the function in the previous function, then use the super syntax again.
```python
class sample():
 a=2
 b=3
 def __init__(self):
     self.a=100
     self.b=50
 def fun(self):
     print("Hello world")
     
     
class sample2(sample):
    def __init__(self):
     super().__init__()
    def fun(self):
        super().fun()
        print(self.a+self.b)
        
mysample2=sample2()
mysample2.fun()

```
```
Hello world
150
```


____

So friends that was all for today. Thank you and hope you are enjoying....

