names=["Aatmaj", "zephyr","123", "163","1723"]
>>> print(names)
['Aatmaj', 'zephyr', '123', '163', '1723']
>>> names.count("zephyr")
1
>>> names.index("163")
3
>>> names.append("A")
>>> len(names)
6
>>> print(names)
['Aatmaj', 'zephyr', '123', '163', '1723', 'A']
>>> lastnames=["L","M","N"]
>>> names.extend(lastnames)
>>> names
['Aatmaj', 'zephyr', '123', '163', '1723', 'A', 'L', 'M', 'N']
>>> names.insert(4, "O")
>>> names
['Aatmaj', 'zephyr', '123', '163', 'O', '1723', 'A', 'L', 'M', 'N']
>>> names.remove("A")
>>> names
['Aatmaj', 'zephyr', '123', '163', 'O', '1723', 'L', 'M', 'N']
>>> names.pop()
'N'
>>> names
['Aatmaj', 'zephyr', '123', '163', 'O', '1723', 'L', 'M']
>>> names.remove(2)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    names.remove(2)
ValueError: list.remove(x): x not in list
>>> names.pop(3)
'163'
>>> names
['Aatmaj', 'zephyr', '123', 'O', '1723', 'L', 'M']
>>> names.reverse()
>>> names
['M', 'L', '1723', 'O', '123', 'zephyr', 'Aatmaj']
