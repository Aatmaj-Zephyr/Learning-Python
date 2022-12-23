  
def GCD (x,y):
    if(x%y!=0):
     return GCD(y,x%y)
    else:
      return y
print(GCD(42,5))
