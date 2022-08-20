# [Learning Python- Intermediate course: Day 3, Recursion in Python](https://dev.to/aatmaj/learning-python-intermediate-course-day-3-recursion-in-python-41ff)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-3-recursion-in-python-41ff)

## Today we will study recursion in Python, make recursive functions to solve problems like like Fibonacci numbers, factorial of a number and the Collatz conjecture.

---

In the previous two parts, we have learnt how to make user-defined functions and make them return values. In case you have missed them, be sure to check them out too!🙂

### What is recursion?

> Recursion is a way of approaching problems which breaks apart complex concepts into smaller and smaller solvable steps.

Recursion is an invaluable programming tool. Recursion is an example of the programming principle- Divide and Rule. It is the method of solving a problem by dividing the original problem into two or more sub problems which are similar to the original problem but smaller in size. The subproblems are further divided and so on. Then, we combine the answers of the sub problems and get the answer to the original problem.

Recursion allows the programmer to concentrate on the key step of an algorithm without initially having to worry about coupling that step with all others.

Recursion is one of the most flexible and powerful tools to solve a complicated problem. When properly implemented, recursion is memory and time efficient. Errors like forgetting the return statement must be avoided, else your program will land in a boom!💥

In case anyone is new with the concept of recursion, here are a few quick references

- [Recursion is not hard: a step-by-step walkthrough of this useful programming technique](https://www.freecodecamp.org/news/recursion-is-not-hard-858a48830d83/)
- [A quick guide to Recursion by example.](https://medium.com/front-end-weekly/a-quick-guide-to-recursion-by-example-c0e7949b8ab6)
- [Recursion for Coding Interviews: The Ultimate Guide](https://www.byte-by-byte.com/recursion/)

#### Sample question 1- Write a recursive version of the collatz conjecture-

```python
def collatz(a):
    count=a[len(a)-1]
    if(count==1):
        return a
    if(count%2==0):
        a.append(count/2)
    else:
        a.append(count*3+1)
    return collatz(a)


print(collatz([7]))
```

```
[7, 22, 11.0, 34.0, 17.0, 52.0, 26.0, 13.0, 40.0, 20.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0]
```

> A common computer programming tactic is to divide a problem into sub-problems of the same type as the original, solve those sub-problems, and combine the results. This is often referred to as the divide-and-conquer method; when combined with a lookup table that stores the results of previously solved sub-problems (to avoid solving them repeatedly and incurring extra computation time), it can be referred to as dynamic programming or memoization. - [Wikipedia](<https://en.wikipedia.org/wiki/Recursion_(computer_science)>)

---

#### Write a program to find the n'th Fibonacci number recursively.

```python
def fibo(n):
    if(n==1 or n==2):
        return 1
    return fibo(n-1)+fibo(n-2)

print(fibo(6))
print(fibo(10))
```

```
8
55
```

### Exercises

- 1. Write the recursive function for factorial of a number.
- 2. Write a program to give the following output **without using the for loop**

```
******
*****
****
***
**
*
```

---

That's all for today. Tomorrow we will check out some more recursive functions and learn the Guidelines of Recursion.
✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
