a=[]
for i in range(0,4):
   try:
    a.append(ord(input("Please enter a character ")))
   except:
    print("Error!")
a=sorted(a)
#The sorted() method sorts the list and returns the sorted list
# This is an inbuilt function to sort the list. You can also use insertion sort.
for i in range(0,len(a)):
    a[i]=chr(a[i])
print(a)
