a=input("Please enter a character ")
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    
 num=(input("Please enter a number "))
 for i in range(0,int(num)):
    for j in range(0,i+1):
        for k in range(0,j+1):
            print(a,end="")
        print("")
    print("")
else:
    print("not a vowel")
