n=int(input("Please enter first number "))
m=int(input("Please enter second number "))
dividend=n
divisor=m

rem=dividend%divisor
while rem>0:
    dividend=divisor
    divisor=rem
    rem=dividend%divisor
gcd=divisor
lcm=(n*m)//gcd
print("gcd= ",gcd,"  lcm= ",lcm)
