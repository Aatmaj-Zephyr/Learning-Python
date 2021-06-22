a=int(input("please enter a number "))
if(a<10):
    print(" 1 digit number")
elif(10<a<100):
    print(" 2 digit number")
elif(100<a<1000):
    print(" 3 digit number")
elif(1000<a<10000):
    print(" 4 digit number")
else:
    print(" 5 digit number")
