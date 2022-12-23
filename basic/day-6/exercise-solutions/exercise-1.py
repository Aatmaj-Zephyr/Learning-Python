a=int(input("Please enter a digit number "))
c=0
while(a>0):
  c=10*c+a%10
  a=a//10
print(int(c))
