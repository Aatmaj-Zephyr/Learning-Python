# [Learning Python- Basic course: Day 2, Statements, Comments and Indentation](https://dev.to/aatmaj/learning-python-basic-course-day-2-statements-comments-and-indentation-5b71)
---
Orininglly published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-2-statements-comments-and-indentation-5b71)


✌️Hi all! Welcome to the second day of the course! Today let us learn about some Python syntax.
---
____

**Statements in Python**
Statements in Python are of three types
 a) *Expressions*- Statements which perform actions like addition, division, or any other such operations.
Here are a few sample commands.
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/63vyhu0x4l4mtuurtkmy.png)
 

b) *Assignments*- The statements giving values to variables are called assignments.
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fx7jfp4nat30849nlf7x.png)
 
c) *Declarations* - Functions, classes in python are declared by using the keyword "def". The function declaration must end with semicolon ":"
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6lq9a7kd4jba8emr8611.png) 

**Indentation in Python**- We need to leave spaces after every loops and function declarations. Brackets in Java are replaced by indentation in Python.
If Indentation is not respected, this error is generated.
 ![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gw6pdo7kylnnxmu1bzvb.png)
Moreover, every loop must end by a semicolon ':'

**Comments in Python** - Comments in Python begin with a '#' These commands are ignored by the interpreter and used to make the program clearer for the developers.

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1ivssdmwsicnf0gghb02.png)

> Comments are an essential part of documentation. Proper documentation is a good programming habit. More about it [here] 
  (https://dev.to/aatmaj/document-today-or-repent-tommorrow-1mg8).

---

Now, let us see a sample Python program-
```python
print("Program to accept student details.") 
#here, print() takes one string argument.

#input()  takes one string argument which it prints out.
#input()  returns one string argument
Rollno=int(input("Enter Roll Number ")) 
#int() converts the string into an integer type

name=input("Please enter a name ")

avg=float(input("enter percentage scored "))
#float() converts the string into an float type

print("Rollno of the student ",Rollno)
print("Name of the student ",name)
print("Percentage scored",avg,"%")
#here print() takes multiple arguments which it prints in the sequential order

```
Output-

![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/anryspmfuk101cb7oc1i.png)
 
Note, that as we need to operate upon the numbers inputted, we have used the int() method.
But if we input a character or string in place of the int, we will get the following error.
![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uflvv8cbm4ouai7uj8z2.png)
 
In order to prevent such errors, error handling must be dont, which will be covered in this course...

Here is another program which gives the value of net resistance in parallel
```python
a=int(input("Please enter first resistance "))
b=int(input("Please enter second resistance "))
c=(a*b)/(a+b)
#write the brackets carefully
print("answer is",c)
```
output-![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/c45pic9jsdzmhfhdq343.png)
More about operators in Python will be in the next blog... 

Exercise----
  1) Write a code in Python to find average of four numbers in one line, without declaring any variables.
  2) Write a code to reverse a three digit number in Python.
(Answers can be found [here](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/da79fe42615a3a3755a78e7df7e1bbd13c35d56a/Basic/Day%202/Exercise%20solutions/Average%20of%20four%20numbers.py))


*To be continued....😏*
____
So friends that's all for this part. 😊 Hope you all are enjoying.😎 Please let me know in the [comment section](https://dev.to/aatmaj/learning-python-basic-course-day-2-statements-comments-and-indentation-5b71) if you liked it or not. 🧐 And don't forget to like the post if you did. 😍 I am open to any suggestions or doubts. 🤠 Just post in the comments [here](https://dev.to/aatmaj/learning-python-basic-course-day-2-statements-comments-and-indentation-5b71) or gmail me. 😉
Thank you for being so patient.👍
