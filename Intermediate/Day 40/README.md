# [Learning Python- Intermediate course: Day 40, Summary of the week and more about OOP](https://dev.to/aatmaj/learning-python-intermediate-course-day-40-summary-of-the-week-and-more-about-oop-5gap)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-40-summary-of-the-week-and-more-about-oop-5gap)

Today let us summarize the week and check out a more about OOP
---
____
Let us first check out a program which shows the implementation of Complex numbers through classes

```python
class Complex:
    #Default values
    x=0
    y=0 
  
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def absolute(self):
        return (self.x**2+self.y**2)**0.5

a=Complex(2,-3)
print(a.absolute())
b=Complex(4,5)
print(b.absolute())
```
```
3.605551275463989
6.4031242374328485

```

In the above program, a and b are different objects of the same class. Which means that they have different values of attributes. Object is representative of class. Consider it like this - class is a common noun while the object is a proper noun. Classes are like templated for molding objects.

_____

> **Why OOP?** 
In software development lifecycle, coding is fifth or sixth stage. First analysis of requirements of clients is done. Developers approach client and get technical review of the requirement, discuss at length with client. Unless we get clarity as what and how is expected coding doesnt start. Then feasibility test is done. budget-wise. then prototype is given to client step by step. Changes are noted. 
In this whole process, the use of OOP is beneficial. Maintaining, updating and carry forward existing versions to next version can be done easily using OOP. Code flexibility is enhanced. We can make changes to the project without much changes in code using OOP. Also, extension of code becomes very easy. We can add new features without much changes to the old ones. This is why in a popular language like Python, learning about OOP is important.

____

### Summary of the week.

#### [Day 37](https://dev.to/aatmaj/learning-python-intermediate-course-day-37-file-handling-in-python-1pih) 
We learnt about file handling in Python. 
We can open a file into four modes
- "r" Reading mode
- "w" Writing mode
- "a" Appending mode
- "r+" Both reading and writing
If not passed, then Python will assume it to be “ r ” by default. `file = open("myfile.txt", "r") ` Opens the file. We can read the contents of the file using the `file.read()` method. We can write into a file using the `file.write("\n")` method. 


#### [Day 38](https://dev.to/aatmaj/learning-python-intermediate-course-day-38-oop-197)
 We learnt about making classes in Python. Classes are object blueprints. Classes are generated using the syntax 
```
def functionname (classname,......arguments......):
 ...
 ...
 ...
 ```
In the class methods, the class parameter (`self`) is a must. Private methods can be made by writing two underscores before the class name. Private methods cannot be accessed from outside the class.

#### [Day 39](https://dev.to/aatmaj/learning-python-intermediate-course-day-38-oop-constructor-init-2lhj)
 Constructors in Python can be created using the `__init__` keyword. A constructor is a special type of member function of a class which initializes objects of a class. The constructor is run when the class is instantiated. The class constructors can be called by other parts of the class or even outside pf the class. If we do not provide a constructor to the class, Python generates one default constructor automatically. We can even pass parameters to the constructors.


____
So friends that was all for today! 
Next week plan-

- Inheritance
- Polymorphism
- Deadly triangle of death
