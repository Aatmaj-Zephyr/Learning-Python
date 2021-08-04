No change at all! 
It will just make the code shorter by eliminating the else  statament., with no change in the output or the way it works.
This is because if the `if` statement runs, then the function code will terminate at the return statement and won't run the next lines.
This is why the else statement is not required.
```python
def isodd(a):
    if(a%2==0):
        return True
    return False
print(isodd(5))
```
```
False
```
