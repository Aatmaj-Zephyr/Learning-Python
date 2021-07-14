a=ord(input("Please enter a letter "))
if(65<=a<=65+26): #65=A
    print(chr(a-65+97))
    #65=A, 97=a 
if(97<=a<=97+26): #65=A
    print(chr(a+65-97))
