import random as rd
# This is shorthand for writing the entire module name over and over again
for i in range(0,5):
 n = rd.randint(1,10) # instead of random.randint() we write rd.randint()
 print(n)
