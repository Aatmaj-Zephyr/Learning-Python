a=[[1,2,3],4,[5,6],[7,[8,9],10],[11,12,13,14],15]
for i in range(0,len(a)):
    try:
     a[i].reverse()
    except:
        pass
print(a)
