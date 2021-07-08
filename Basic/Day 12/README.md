# [Learning Python- Basic course: Day 12, Basic algorithms](https://dev.to/aatmaj/learning-python-basic-course-day-12-basic-algorithms-1edc)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-basic-course-day-12-basic-algorithms-1edc)

Today let us explore Sequential search, Binary search and Bubble sort in Python.🚀
---
____

Today we will check out sequential search, binary search and bubble sort in Python lists. We will not go into the mathematical details of the complexity and all but just see how the algorithms are implemented. More complicated searching and sorting algorithms, complex data structures will be referenced and covered in the later parts. In case anyone among you are coming across these algorithms for the first time, please do google these terms out. I have also provided Geeksforgeeks references for further reading.

### Sequential search
The sequential search is the most easy and simple program for searching. We can just traverse through the list or use the inbuilt `in` method.

```python
a=[1,3,4,6,5,2,6]
n=int(input("Please enter the number to be searched "))
#Method-1
for i in range(len(a)):
    if (a[i]==n):
        print("Method-1 Yes, the number is in the list ")
        break

#Method-2
if(n in a):
    print("Method-2 Yes, the number is in the list ")
```
Output
```
Please enter the number to be searched 6
Method-1 Yes, the number is in the list 
Method-2 Yes, the number is in the list 
```

Python provides a shortcut for searching as shown in method 2. This is a sequential search method for searching. It can search not only numbers, but characters or any other data types as well.

### Binary search
Binary search is another simple algorithm to search for numbers in a sorted list. In case you are new with Binary search, see [GeeksForGeeks](https://www.geeksforgeeks.org/binary-search/)

```python
a=[1,3,5,6,8,7,10,12,14]
x=int(input("Please enter a number "))
low = 0
high = len(a) - 1
mid = 0
while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if (a[mid] < x):
            low = mid + 1
        # If x is smaller, ignore right half
        elif (a[mid] > x):
            high = mid - 1
        # means x is present at mid
        else:
            print(mid+1)
            break     
```
Output-
```
Please enter a number 6
4
```
### Bubble sort
Bubble sort is a good sorting algorithm, and quite easy comparatively. more about it on [GeeksForGeeks](https://www.geeksforgeeks.org/bubble-sort/)
```python
a=[2,4,3,7,6,5,9,10,12]
 # Traverse through all array elements
for i in range(len(a)):
    # Last i elements are already in place
    for j in range(0, len(a)-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if (a[j] > a[j+1]) :
                (a[j], a[j+1]) = (a[j+1], a[j]) #Swapping the two
 
print ("Sorted array is:",a)
```

Output-
```
Sorted array is: [2, 3, 4, 5, 6, 7, 9, 10, 12]
```
### Exercises-
1) & 2) In the samples above, the programs give no output if the item is not in the list. Modify the programs to include it. Answers - [Sequential search](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/97d78151fd6bfccb02ac1da1c042f807d08c6f06/Basic/Day%2012/Exercise%20solutions/Exercise%201.py), [binary search](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/97d78151fd6bfccb02ac1da1c042f807d08c6f06/Basic/Day%2012/Exercise%20solutions/Exercise%202.py)

3) Write a program to bubble sort a list and then search using binary search. [Answer](https://github.com/Aatmaj-Zephyr/Learning-Python/blob/97d78151fd6bfccb02ac1da1c042f807d08c6f06/Basic/Day%2012/Exercise%20solutions/Exercise%203.py)

____

😎 Your suggestions motivate me, so please please please let me know in the [comment section on dev.to](https://dev.to/aatmaj/learning-python-basic-course-day-12-basic-his repoalgorithms-1edc) if you this part or not. 
🧐 And don't forget to like the post if you did. 😍 Follow me on github and star t
