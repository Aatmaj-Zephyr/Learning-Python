# [Learning Python- Intermediate course: Day 7, Making Python modules](https://dev.to/aatmaj/learning-python-intermediate-course-day-7-making-python-modules-kmf)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-7-making-python-modules-kmf)

We have learnt how to use predefined python modules. Today we will create our very own Python module. 🤩 So put your seatbelts on for this thrilling Python journey🚀
---
____
### Modules in Python

Creating a module in Python is a very easy task. ![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gimh5787334irbtozlp6.png)

- **Step I** Make a python file named mymodule.py *(or any other name ending with `.py`)* which contains various functions. Do this in Python IDLE or any other IDE.
 Here is a sample file-
```python
def hi():
    print("hi")
def hello():
    print("hello")
def add(a,b):
    return a+b
def printer(a):
    print(a)    
```

- **Step II** Save the python file (or copy-paste the file) in the Lib (not libs) folder of the Python source code.
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/p0h2lhupyhf1kvi16htj.png)
 
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lch7es61p6z5h4omr62o.png)
 

- **Step III** In the file in which you want to use the module, write `import mymodule` *(import the relevant module name)* After that, just use the functions in the module as predefined functions. Simple !!

Here is the program which uses the functions in our module.
```python
import mymodule
mymodule.printer("Welcome to Python intermediate course!")
print(mymodule.add(2,3))
mymodule.hello()
```
We now save it in a file named 'mymoduletester' and run it.
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/38ckjf3y6kcdx9tiiuhs.png)
 
After we run the file, an output is generated in a command line window.
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6nyx30dz7bw9ptrzucz9.png)
 
OUTPUT-
```
Python 3.10.0a2 (tags/v3.10.0a2:114ee5d, Nov  3 2020, 00:37:42) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/aatma/AppData/Local/Programs/Python/Python310/Lib/mymoduletester.py
Welcome to Python intermediate course!
5
hello
 
```

That's it! We have successfully made our own module and used it in our code!🤓 Cool!😎

I have used the IDLE for Python over here, but you are free to use any editor you want. We can have the same effect by using the online GDB compiler as shown below.
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/175gnpj0k8xzvqi8kct2.png)
 
____
✌️So friends that's all for now. 😊 Hope you all are having fun.😎 Please let me know in the comment section below 👇. And don't forget to like the post if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the comments below or gmail me. 😉
Thank you all👍

Also please visit the [Learning-Python repo](https://github.com/Aatmaj-Zephyr/Learning-Python) made especially for this course and don't forget to star it too
