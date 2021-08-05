def collatz(a):
    count=a[len(a)-1]
    if(count==1):
        return a
    if(count%2==0):
        a.append(count/2)
    else:
        a.append(count*3+1)
    return collatz(a)


print(collatz([7]))
