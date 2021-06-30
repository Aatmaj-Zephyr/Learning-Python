No. we cannot replace, it because in the program chr takes input i, which is a number while ord requires a string input.
```python
Istrue=True
#Istrue is a boolean value with value default True
for i in range(1,1000):
 a=ord(i)
 if(i!=chr(a)):
     Istrue=False
print(Istrue)
```
OUTPUT-
```
Traceback (most recent call last):

  File "main.py", line 4, in <module>

    a=ord(i)

TypeError: ord() expected string of length 1, but int found

```
