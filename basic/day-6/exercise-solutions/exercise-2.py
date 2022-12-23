n=int(input("Please enter a number "))
den=2
temp=n
while temp>1:
     rem=temp%den
     if rem==0:
         print(den,end=" ")
         temp//=den
     else:
         den+=1
         
