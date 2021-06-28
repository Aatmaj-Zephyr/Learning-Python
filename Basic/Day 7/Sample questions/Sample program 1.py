a=0
b=1
print('0,1,',end="")
for i in range(0,10):
   a,b=b,b+a
   print(b,end=",")
