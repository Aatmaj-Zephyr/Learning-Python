a={1:10, 2:20}
b={3:30, 4:40}
c={}
for i in (a,b): 
    #for every element in dictionary a AND dictionary b,
    c.update(i)
    #update the dictionary to include these values.
print(c)
