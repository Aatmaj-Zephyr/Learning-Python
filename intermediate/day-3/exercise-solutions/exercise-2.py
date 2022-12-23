def printer(a,b):
    if(b!=0):
      if(a!=0):
          print("*",end="")
          printer(a-1,b)
      else:
          print()
          printer(b-1,b-1)
printer(6,6)
