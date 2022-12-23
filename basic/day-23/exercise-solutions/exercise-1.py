a="helloworld"

if(a.isalnum()==True):
    if(a.isdigit()):
        print("Numeric")
    elif(a.isalpha()):
        print("Alphabet")
    else:
        print("Alphanumeric")
else:
    print("Not alphanumeric")
