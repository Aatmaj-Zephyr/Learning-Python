NO CHANGES AT ALL! This is because Python doesn't care about type safety.
In the function, whatever parameter you pass has only one condition, that is the code must be compatable with it.
Here, the for loop was compatable with both- list as well as tuples.
Hence if we pass any of them, it will not make any difference

```python
def prod(a):
    temp=1
    for i in a:
        temp*=i
    print(temp)
prod((1,2,3,4))
prod([1,2,3,4])
```

OUTPUT-

```
24
24
```
