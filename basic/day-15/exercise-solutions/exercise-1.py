a=(input("Please enter a number "))
try:
    a=int(a)
    b=15-a
    try:
        c=chr(b)
        #chr() of negative numbers generates an error,
        # so if a>15, then the except condition will run,
        # if a>=15, then this will run
        try:
            b=1/b
            #if a=15, b=0,and thus error generated
            print("Number less than 15")
        except:
            #zero error generated, so a=15
            print("Number is equal to 15")
    except:
        print("Number greater than 15")
except:
    print("You did not enter a string ")
