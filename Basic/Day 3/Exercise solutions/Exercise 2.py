a=int(input("Enter a number "))
if a>0:
 if a%2==0:
  print(a," is a positive even number")
 else:
  print(a," is a positive odd number")
elif a<0:
 if a%2==0:
  print(a," is a negative even number")
 else:
  print(a," is a positive odd number")
else:
 print(a," is even and zero.")
