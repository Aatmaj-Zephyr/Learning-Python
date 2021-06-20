a=int(input("Please enter a 3 digit number "))
a=(a%10)*100+(a%100-a%10)+(a%1000-a%100)/100 #standered algorithm to reverse a number
# the % is the modulo operator
print(int(a))
#the int in the print prevents trailing zeros.
#Exercise- try the code without int() in print.
