a=[1,2,3] #list
b=(1,2,3) #tuple
c=[b,2,4] #list
d=(1,b,c) #tuple
check=[a,b,c,d] 
for i in check:
    try:
        i.append(1)
        print(i," is a List")
    except:
        print(i," is a Tuple")
