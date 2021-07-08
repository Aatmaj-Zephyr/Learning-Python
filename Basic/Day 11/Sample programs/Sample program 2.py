a=[]
r=int(input("Please enter the number of rows "))
c=int(input("Please enter the number of columns "))
for i in range(r):
    #Append an empty sublist
    a.append([])
    for j in range(c):
        num=int(input("Enter a value "))
        a[i].append(num)

print(a)
for i in a:
     for j in i:
         print(j, end="\t")
         #here, "\t" stands for tab, i.e. leave spaces
     print()
