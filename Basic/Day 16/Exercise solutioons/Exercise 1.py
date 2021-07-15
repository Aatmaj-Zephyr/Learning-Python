a=[1,2]
for i in range(0,3):
    temp=a.copy()
    a.append(temp)
print(a)
for i in range(0,len(a)):
    try:
        print(len(a[i]),end="")
    except:
        print(1,end="")#if not a list
