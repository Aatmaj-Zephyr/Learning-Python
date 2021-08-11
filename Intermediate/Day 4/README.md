# [Learning Python- Intermediate course: Day 4, Summary of the week, Guidelines for Recursion and high-level questions.](https://dev.to/aatmaj/learning-python-intermediate-course-day-4-summary-of-the-week-guidelines-for-recursion-and-high-level-questions-445)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-4-summary-of-the-week-guidelines-for-recursion-and-high-level-questions-445)

Today we will study principles of recursion and then solve questions related to recursion. This is the continuation of the last part, so in case you have missed that one, make sure to have a quick check [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-3-recursion-in-python-41ff)
---
____ 
### Summary of the week-
- [Day 1](https://dev.to/aatmaj/learning-python-intermediate-course-day-1-user-defined-functions-1kg7) We learnt how to make user defined functions. User defined functions are custom  functions designed by the programmer. They provide code reusability and flexibility while solving complicated problems. All this was backed up with two sample questions and one conceptual exercise.

- [Day 2](https://dev.to/aatmaj/learning-python-intermediate-course-day-2-returning-values-from-methods-4bhn) We learnt how to return values from functions. By breaking complicated operations into functions, we can make the code more compact and flexible. This is possible because we can return data-types back to the function call. Returning multiple values is invalid, but we can return a list which can hold the values. 

- [Day 3](https://dev.to/aatmaj/learning-python-intermediate-course-day-3-recursion-in-python-41ff) We studied recursion in Python. We implemented it by calling the function from inside it. We then solved some good questions related to recursion.


### Guidelines for using recursion.
> Recursion is a tool to allow programmer to concentrate on the key step of an algorithm, without initially having to worry about how to couple that step with the others.

Recursion is basically breaking apart a problem into parts, solving a single part and the while problem gets solved magically. 

Consider an example. We want to find the shortest path to a city. So first, we find shortest paths to all it's neighboring cities, and then choose the route which is smallest. And how do we find the shortest path to the neighboring cities? Well in the same way! This is the beauty of recursion. We can address a complicated problem by making smaller replicas to the main problem on and forever! This is known as the travelling salesman problem, which we solved using recursion.

We first start any problem by asking *"How can this problem be divided into parts?"* Once we have a simple short step to solve a mini-problem of the same type, applying it to a larger problem is easy.

Finally we need to decide a stopping rule to prevent the recursion from running indefinitely. For example in the above problem, we stop when we reach to the city from where we have to start.

### Exercises
- The *Greatest Common Divisor* (GCD) of two positive integers is the largest integer that divides both of the two integers. Thus, the GCD of 8 and 12 is 4, the GCD of 9 and 18 is 9, and the GCD of 16 and 25 is 1. Write a recursive function namd `GCD (x,y)` that implements this *division algorithm*: if y=0, then the GCD of x and y is x; otherwise the GCD of x and y is the same as the GCD of y and x%y. 

- The binomial coefficients may be defined by the following recurrence relation, which is the idea of the pascal's triangle.
`C(n,0)=1 and C(n,n)=1 for n>=0`
`C(n,k)=C(n-1,k)+C(n-1,k-1) for n>k>0`
Write a recursive function which will generate C(n,k) by using the above formula

- The *Ackermann's function*, defined as follows, is a standered device to determine how well recursion is implemented in any device.
```
A(0,n)=n+1                for n>=0
A(m,0)=A(m-1,1)           for m>0
A(m,n)=A(m-1,A(m,n-1))    for m>0 and n>0 
```

> Yes, the above exercises are a bit difficult. But the key is finding C(n,k) or A(m,n) and directly implementing it. The rest is just about when to stop the recursion conditions. All the best for solving them! Solving these exercises will make you all fluent with recursion and it's problem solving  principles.

### [All Answers here](https://github.com/Aatmaj-Zephyr/Learning-Python)
____
*A bit about the course*
I know, I am going a bit slow for some of you.  But this is for the benifit of those who are here for the first time. This week was a gentle intro to user defined functions. In the coming weeks, I will cover all the details of the language. For those who already know coding basics, they can just skim through the blog and mull upon the exercises. The exercises provided will strengthen and reinforce the concepts. Moreover they are directly taken or similar to past coding tests from the interview panel...


🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
Follow me on GitHub for updates.........
