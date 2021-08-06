  def C(n,k):
    if(k==0):
       return 1
    if(n==k):
       return 1
    return C(n-1,k)+C(n-1,k-1)
for i in range(0,100):
  for j in range(0,i+1):
      print(C(i,j),end="")
  print()
