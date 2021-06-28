a=int(input("Enter a number "))
IsPrime=0
n=2
while(n<a//2):
    if (a%n==0):
        print("The number is composite ")
        IsPrime=1
        break
    n=n+1
if (IsPrime==0):
 print("The number is prime.")
