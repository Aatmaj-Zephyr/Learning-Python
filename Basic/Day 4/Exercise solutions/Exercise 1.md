### Bug one. Range begins from zero.
The range can;t begin from zero. Because if it does, then the first value of i will be 0, and integer division be zero is not possible. This will result in the following error
```
Enter a number 10

Traceback (most recent call last):

  File "main.py", line 3, in <module>

    if n%i==0:

ZeroDivisionError: integer division or modulo by zero
```


### Bug two: while loop must end with n+1 and not n
Let us say that we consider the input 10. The last value of the i will be 9 and not 10. Hence the result will be 
```
Enter a number 10
1
2
5
```

But we want the number 10 to be included in the set of divisors. Hence we put n+1 at the ending bracket.
