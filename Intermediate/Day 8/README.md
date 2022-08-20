# [Learning Python- Intermediate course: Day 8, Summary of the week and nested Modules](https://dev.to/aatmaj/learning-python-intermediate-course-day-8-summary-of-the-week-and-nested-modules-j3d)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-8-summary-of-the-week-and-nested-modules-j3d)

Hello friends, today we will summarize the learning of the week.

### Summary of the week

- [Day 5](https://dev.to/aatmaj/learning-python-intermediate-course-day-5-exploring-the-math-module-5alo) We learnt that modules are a way of packaging our code which enhances flexibility and code reusability. Modules are basically python files which contain various functions. One example of which is the built in module math. The math module in Python is a very useful module. We can perform various mathematical functions using the module.
- [Day 6](https://dev.to/aatmaj/learning-python-intermediate-course-day-6-math-exercises-12ge) In this part we solved many questions related to the math module for example Armstrong numbers, use of recursion in solving power operations, etc.
- [Day 7](https://dev.to/aatmaj/learning-python-intermediate-course-day-7-making-python-modules-kmf) We saw how to make our own Python modules and how to use them in our code. We can make Python module by saving a Python file (with the `.py` extension in the Lib folder of Python source. Then we can use the modules by using the import statement.

### Using modules in modules

We can use a module in another module.
Here is a sample question-

Create a module named ModuleC to calcuate the combination of two numbers. This module must import ModuleB which contains the factorial function.

- ModuleB

```python
def factorial(A):
    if(A<=0):
        return 1
    else:

        return A*factorial(A-1)
```

- ModuleC

```python
import ModuleB
def comb(n,r):
    return ModuleB.factorial(n)/(ModuleB.factorial(r)*ModuleB.factorial(n-r))
```

- main

```python
import ModuleC
print(ModuleC.comb(5,2))
```

```
10.0
```

What will happen if we try to call the function factorial from he main? We cannot do so as the main does not directly import ModuleB. Hence, we cannot use the factorial defined in B as ModuleC.factorial() or ModuleB.factorial()

```python
import ModuleC
print(ModuleC.comb(5,2))
print(ModuleC.factorial(4))
```

```
10.0
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    print(ModuleC.factorial(4))
AttributeError: 'module' object has no attribute 'factorial'
```

```python
import ModuleC
print(ModuleC.comb(5,2))
print(moduleB.factorial(4))
```

```
10.0
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    print(moduleB.factorial(4))
NameError: name 'moduleB' is not defined

```

For the above code to run, we need to import the module B.

```python
import ModuleC
import ModuleB
print(ModuleC.comb(5,2))
print(ModuleB.factorial(4))
```

```
10.0
24
```

---

- We all know that neither me nor you have ever seen each other. Learning in remote environment is a difficult, and teaching is perhaps even more difficult. Teaching is never a one-way process.
  I request everyone to participate actively in this course, either through comments below or forking on Github [Learning-Python repo](https://github.com/Aatmaj-Zephyr/Learning-Python)
  😃 😃 😃

> For those who have not yet made account in Dev.to, you can have a free easy sign-up using your mail or GitHub accounts. I would suggest the budding developers to create your GitHub free account right away. You would require to register sooner or later anyways

🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
Next day will begin from Tuesday📅
