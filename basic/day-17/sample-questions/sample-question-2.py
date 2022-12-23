a=[]
for i in range(0,4):
    a.append(ord(input("Please enter a letter ")))
for i in range (0,len(a)):
 if(65<=a[i]<=65+26): #65=A
    print(chr(a[i]-65+97))
    #65=A, 97=a 
 elif(97<=a[i]<=97+26): #65=A
    print(chr(a[i]+65-97))
 else:
    print("Error. Please enter only characters.")
