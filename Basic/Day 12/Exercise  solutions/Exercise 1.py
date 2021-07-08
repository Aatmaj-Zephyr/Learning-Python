a=[]
for i in range(2,100):
    isprime=True
    for j in range(0,len(a)):
        if(i%a[j]==0):
           isprime=False
           break
    if (isprime==True):
        a.append(i)
print(a)
