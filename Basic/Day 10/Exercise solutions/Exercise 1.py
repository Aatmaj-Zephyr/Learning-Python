a=[]
SmallestValue=0
GreatestValue=0
n=int(input("Please enter a number "))
for i in range(0,n):
    a.append(int(input("Please enter a number "))) 
#If we forget to put the int() function ivee here, too many errors will get generated
for i in (0,len(a)-1):
 if(a[i]<SmallestValue):
     Smallestvalue=a[i]
 elif(a[i]>GreatestValue):
     GreatestValue=a[i]
print("Smallest value= ",SmallestValue," Greatest value= ",GreatestValue)
