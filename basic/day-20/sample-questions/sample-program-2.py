a={}
for i in range(0,10):
    b=int(input("Please enter a number "))
    key=b%10
    try:#append to original list exists.
     if key not in a[key]:
      a[key].append(b)
    except:#make a new list
        a[key]=[b]
print(a)

#retrieving the key
b=int(input("Please enter the value"))
key=b%10
print(a[key].pop(b))
