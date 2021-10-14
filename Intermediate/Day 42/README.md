# [Learning Python- Intermediate course: Day 42, Polymorphism.](https://dev.to/aatmaj/learning-python-intermediate-course-day-42-polymorphism-a61)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-42-polymorphism-a61)

Today we will learn about Polymorphism in Python
---
____
### What exactly is Polymorphism
Polymorphism is an OOP feature which provides extensibility and flexibility to your code. The major advantage of Polymorphism is flexibility. Polymorphism gives you the the flexibility lost in inheritance. 

> **Poly** - many 
**morphism** -many forms
**Polymorphism** is the condition of occurrence in different forms.

#### Polymorphism in operators
We use polymorphism when dealing with operators. For example the `+` operator is used to add two numbers as well as to coconcate two strings. In the same way, the product operator `*` is used to multiply two integers, floating numbers as well as two complex numbers in Python. This is an example of polymorphism which we have unknowingly used until now.

#### Polymorphism in functions
Till now we have come across many functions which take in arguments of various multiple types. For example the print function takes in lists, tuples, numbers, complex numbers as well as strings. Another example is the `len()` function which takes in any iterable type. when string is passed, it returns the number of characters, when list is passed it returns the number of elements and when a dictionary is passed, it returns the number of key values.


____

### Polymorphism in OOP
Let us now study what is polymorphism in classes and how does it turn out to be useful.
Yesterday we saw how the methods with same name are overridden. Polymorphism is something related to functions with the same name. In order to understand what polymorphism is, let us consider the following example. 

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
        
a=chimpanzee(20)
b=chimpanzee(25)
c=gorrilla(50)

a.cry()
b.cry()
c.cry()

print(a.weight)
print(b.weight)
print(c.weight)

a.eat()
b.eat()
c.eat()
```
```
I am a chimp
I am a chimp
I am a gorrilla
20
25
50
bananas
bananas
fruits

```

> Study the above example carefully.  What we have seen above is an example of polymorphism itself!



Now, chimpanzee and gorilla both derive from the same class- ape. They have same attributes- weight and food. But they have different values for them. We can even add additional  methods for each of those classes. But the attributes weight, food, and method eat was derived from the class ape itself. So is there a way to use them without knowing weather the ape is a chimpanzee or a gorilla? This is possible if all of them have same methods (that is overloaded methods.) In other words can we just use their 'apish' characteristics as one by using the methods. This is the central idea behind polymorphism. In Python, Polymorphism is achieved through method overloading.

`a` is both a ape as well as a chimpanzee. So can we treat a as n ape? so can we treat `a`, `b`, `c` as equal apes? We can using polymorphism. At times, we may need to consider that `a,b,c` are just apes and not gorillas or chimpanzees and treat them all equally. This decreases the overhead of treating objects of different subclasses species as different entities. For example tomorrow if I want to add an Orangutan subclass, I will not require to go back and change everything I had written earlier. Using Polymorphism I can just treat them as equals. We overload the functions.

Now we can make the polymorphism better by using 

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
  
       
a=chimpanzee(20)
b=chimpanzee(25)
c=gorrilla(50)

for i in (a,b,c):
 i.cry()
 print(i.weight)
 i.eat()
```


____

So friends that was all for today. Let us learn more about Python in the upcoming days.....

