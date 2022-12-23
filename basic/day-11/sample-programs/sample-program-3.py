>>> a=('Aatmaj','Zephyr',163,'1234')
>>> b=(1,2,3,4,5)
>>> c='a','b','c','d'
>>> print(a)
('Aatmaj', 'Zephyr', 163, '1234')
>>> print(len(a))
4
>>> print(a[3])
1234
>>> d=((1,2,3),a,b,('a','c','2',5))
>>> print(d)
((1, 2, 3), ('Aatmaj', 'Zephyr', 163, '1234'), (1, 2, 3, 4, 5), ('a', 'c', '2', 5))
>>> print(len(d))
4
>>> print(len(d[1]))
4
>>> print(d[2][3])
4
>>> print(d[4][2])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> a.append(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
