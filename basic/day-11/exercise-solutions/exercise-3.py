a=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(a)):
    for j in range(i+1):
        print(a[i][j],end="")
    print()
