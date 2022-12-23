names=[] #Declaration of the list without value
print(len(names))
num=int(input("Enter number of Names to be stored in a list "))
for i in range(0,num):
    st=input("Enter a name ")
    names.append(st)
print("Values stored in List: ")
for i in range(0,num):
    print(names[i])
