b={
    1:[1],
    2:[1,2],
    3:[1,2,3],
    4:[1,2,3,4],
    5:[1,2,3,4,5]
}
b={}
for i in range(1,6):
    b[i]=[]
    for j in range(1,i+1):
        b[i].append(j)
print(b)
