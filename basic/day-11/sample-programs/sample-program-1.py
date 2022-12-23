>>> list=[[1,2,3],[2,3,4],[3,4,5]]
>>> print(list[1])
[2, 3, 4]
>>> print(len(list))
3
>>> print(list[2][1])
4
>>> print(len(list[0]))
3
>>> print(list)
[[1, 2, 3], [2, 3, 4], [3, 4, 5]]
>>> for i in range(0,len(list)):
...  for j in range(0,len(list[i])):
...   print(list[i][j])
...
1
2
3
2
3
4
3
4
5
>>> for i in list:
...  for c in i:
...   print(c,end="")
...  print()
...
123
234
345
