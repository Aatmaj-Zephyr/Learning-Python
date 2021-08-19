import random 
for i in range(0,5):
 n = random.randint(7,5) #wont run as order is not ascending
 print(n)
'''
Error message will be generated as follows-



Traceback (most recent call last):
  File "main.py", line 3, in <module>
    n = random.randint(10,7)
  File "/usr/lib/python3.4/random.py", line 218, in randint
    return self.randrange(a, b+1)
  File "/usr/lib/python3.4/random.py", line 196, in randrange
    raise ValueError("empty range for randrange() (%d,%d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (10,8, -2)
'''
