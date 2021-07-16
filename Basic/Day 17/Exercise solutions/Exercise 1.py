a=[]
for i in range(0,4):
   try:
    a.append(ord(input("Please enter a character ")))
   except:
    print("Error!")
for i in range(1, len(a)):
    for j in range(0,i):
        if(a[j]<a[i]):
            (a[j],a[i])=(a[i],a[j])#swap
for i in range(0,len(a)):
    a[i]=chr(a[i])
a.reverse()#ascending order
print(a)
