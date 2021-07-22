a={1:10, 2:20}
b={3:30, 4:40 , 2:60}
c={}
d={}
for i in (a,b): 
    c.update(i)
print(c)
for i in (b,a): 
    d.update(i)
print(d)
