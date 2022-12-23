a=int(input("Please enter value for a "))
b=int(input("Please enter value for b "))
c=int(input("Please enter value for c "))
if(b**2)-4*a*c>=0:
    print("Answer is", (-b+((b**2)-4*a*c)**0.5)/(2*a))
    #Be carefull of the paranthesis
else:
    print("No real root")
