a=input("Please enter a number ")
try:
    b=int(a)
    print(b)
except:
    print("OPPS! You entered a non-numeric character! ")
finally:
    print("Bye!")
