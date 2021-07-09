a=[]
for i in range(1,10):
 b=i
 a.append([]) #Append an empty list into a list
 while(b!=1):
    a[i-1].append(int(b))
    #int() to prevent trailing  decimal 0. eg 5.0 will be written as 5
    if(b%2==0):
        b=b/2
    else:
        b=3*b+1
 a[i-1].append(1)
print(a)
