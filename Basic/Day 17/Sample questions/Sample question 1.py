a=[1,4,3,5,2]
for i in range(1, len(a)):
    #key = a[i]
    for j in range(0,i):
        if(a[j]<a[i]):
            (a[j],a[i])=(a[i],a[j])#swap
print(a)
'''
Logic-
Set the key equal to the first unsorted value.
Compare the key and the sorted elements.
Move the key to the required position.
'''
