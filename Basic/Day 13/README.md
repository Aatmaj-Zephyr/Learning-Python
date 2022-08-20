# [Learning Python- Basic course: Day 13, Summary of the week and Stack implementation](https://dev.to/aatmaj/learning-python-basic-course-day-13-summary-of-the-week-and-stack-implementation-1b56)

Originally published on the [Dev.to platform here](https://dev.to/aatmaj/learning-python-basic-course-day-13-summary-of-the-week-and-stack-implementation-1b56)

## Today let us generate multidimensional Collatz lists, simulate Stacks and Queues and write out biggest piece of code yet...

---

## Summary of the week-

- [Day 10](https://dev.to/aatmaj/learning-python-basic-course-day-10-lists-in-python-1hcb) We learnt about lists in Python, and various list functions like popping, appending, copying and much more. We then used these functions for creating a program for dynamic generation of lists.

- [Day 11](https://dev.to/aatmaj/learning-python-basic-course-day-11-multidimensional-lists-and-tuples-3bfl) We learnt about multidimensional lists, dynamic generation of multidimensional lists and had an introduction to tuples. We learnt that tuples were non mutable lists.

- [Day 12](https://dev.to/aatmaj/learning-python-basic-course-day-12-basic-algorithms-1edc) We used lists to make algorithms like bubble sorting, binary searching and sequential searching.

## Sample questions

Before going to stacks and queues, let us first check out an application of the dynamic generation of multidimensional lists.

1. Make a multidimensional list which stores the sequence of the Collatz conjecture for integers 1-10.

```python
a=[]
for i in range(1,10):
 b=i
 a.append([]) #Append an empty list into a list
 while(b!=1):
    a[i-1].append(int(b))
    #int() to prevent trailing  decimal 0. eg 5.0 will be written as 5
    if(b%2==0):
        b=b/2
    else:
        b=3*b+1
 a[i-1].append(1)
print(a)
```

Output-

```
[[1], [2, 1], [3, 10, 5, 16, 8, 4, 2, 1], [4, 2, 1], [5, 16, 8, 4, 2, 1], [6, 3, 10, 5, 16, 8, 4, 2, 1], [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], [8, 4, 2, 1], [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]]
```

2. **Implementation of a Stack** -

Implement a stack, with LIFO (Last in first out). The user can push, pop, and print the stack anytime.

> This is the largest program we have ever written so far. See those nesting levels? But do not worry, everything is properly explained in the comments beside the code. For those new to LIFO and FIFO, please visit the [Stack data structure](https://www.geeksforgeeks.org/stack-data-structure)

```python
print("Please enter 'pop' for popping, 'push' for pushing, print to print and end to terminate the program.....")
stack=[] #make a list named 'stack'
while (True):
    a=input("...") #get input from the user
    if(a=='push'):
        while True: #To check if the input is a number or not
         a=input("Which number to push?... ")
         if(48<=ord(a)<=57): #check
            stack.append(a)  #push the number
            break
#if the input is number, then terminate the nested while loop,
# else continue the loop until numeric value is obtained
         else:
            print("Please enter only numbers ") #error return
    elif(a=='pop'):
        print(stack.pop()) #pop, ie. remove and return
    elif(a=='print'):
        print(stack) #print the list
    elif(a=='end'):
        break  #terminate the while loop
    else:
        print("Unknown command ")
print("Thank you")
```

Output-

```
Please enter 'pop' for popping, 'push' for pushing, print to print and end to terminate the program.....
...push
Which number to push?... 3
...poppp
Unknown command
...pop
3
...push
Which number to push?... 4
...push
Which number to push?... k
Please enter only numbers
Which number to push?... l
Please enter only numbers
Which number to push?... 5
...print
['4', '5']
...pop
5
...print
['4']
...push
Which number to push?... 3
...end
Thank you
```

---

---

## Exercises-

1. Write a program to make a list of prime numbers in an effective way. First store prime numbers in an list, then next prime number is the one which is not divisible by the previous prime numbers.

2. Our stack implementation program has many hitches. Some error handling will be covered later on, but now we will focus particularly on this error-

```
Please enter 'pop' for popping, 'push' for pushing, print to print and end to terminate the program.....
...push
Which number to push?... 3
...push
Which number to push?... 2
...pop
2
...pop
3
...pop
Traceback (most recent call last):
  File "main.py", line 16, in <module>
    print(stack.pop()) #pop, ie. remove and return
IndexError: pop from empty list
```

This error is caused by popping from an empty list. Modify the program to error check this, and gove this output-

```
Please enter 'pop' for popping, 'push' for pushing, print to print and end to terminate the program.....
...push
Which number to push?... 2
...pop
2
...pop
Cannot pop from an empty list
...

```

Answer is in the learning Python repo, but I would like everyone to fork the [sample program](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/4eefd0ae6e52bda6cb99360d3a0ae254e00bff1a/Basic/Day%2013/Sample%20questions/Sample%20question%202.py) we did earlier and open a 'pull request' for this modification. For those new with Pull requests, [here](https://opensource.com/article/19/7/create-pull-request-github) is a guide.

3. Write a program for implementation of queue FIFO data structure. [Hint- modify the Stack implementation.](https://www.geeksforgeeks.org/difference-between-stack-and-queue-data-structures/)

Sample output-

```
Please enter 'Add' for Adding, 'Remove' for removing, print to print and end to terminate the program.....
...Add
Which number to Add?... 4
...Add
Which number to Add?... 5
...Add
Which number to Add?... 6
...remove
Unknown command
...Remove
4
...print
['5', '6']
...Remove
5
...Remove
6
...print
[]
...Remove
Cannot Remove from an empty list
...end
Thank you
```

Again, answer is in this repo, but please fork it and try on your own🙂

---

- We all know that neither me nor you have ever seen each other. Learning in remote environment is a difficult, and teaching is perhaps even more difficult. Teaching is never a one-way process.
  I request everyone to participate actively in this course, either through [comments on dev.to](https://dev.to/aatmaj/learning-python-basic-course-day-13-summary-of-the-week-and-stack-implementation-1b56) or forking on this Github [Learning-Python repo](https://github.com/Aatmaj-Zephyr/Learning-Python)
  😃 😃 😃

> For those who have not yet made account in Dev.to, you can have a free easy sign-up using your mail or GitHub accounts. I would suggest the budding developers to create your GitHub free account right away. You would require to register sooner or later anyways
