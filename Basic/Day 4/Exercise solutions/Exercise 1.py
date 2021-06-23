#bug one- the range of the for loop must begin from one and not zero.
# bug two- the range of the while loop must end with n+1 and not n
n=int(input("Enter a number "))
for i in range (1,n+1):
  if n%i==0:
    print(i)
