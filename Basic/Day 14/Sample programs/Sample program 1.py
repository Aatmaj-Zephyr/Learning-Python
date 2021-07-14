a=input("Please enter a number ")
try:
    b=int(a)
    print(b)
except:
    print("OOPS! You entered a non-numeric character! ")
finally:
    print("End of program!")
