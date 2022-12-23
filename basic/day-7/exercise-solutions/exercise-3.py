a=int(input("Enter a number "))
for n in range(0,a):
 s=0
 for i in range (1,n):
  if n%i==0:
    s+=i
 if (s==n):
  print(n," is a perfect number")
