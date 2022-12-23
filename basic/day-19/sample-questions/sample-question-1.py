a=["a","b","c","d"]#list -key
b=(1,2,3,4)#tuple- value

#Method 1
c={} #empty dictionary
for i in range(0,len(a)):
    c[i]=a[i]
print(c)

#Method 2
d=dict(zip(a,b))
print(d)
