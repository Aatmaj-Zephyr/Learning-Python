mport cmath
z = complex(1,1)
a = cmath.polar(z)
print ("The polar complex number is : ",end="")
print (a) # returns a tuple
z2= cmath.rect(a[0],a[1])
print ("The rectangular form of complex number is : ",end="")
print (z2)
