a={}
for i in range(0,5):
    b=ord(input("Please enter a character "))
    key=b%10 #very simple hash function for length 10
    try:
        int(a[key]) 
        #to check if the element is already present in the position or not.
        print("error-- value occupied!")
    except:
           a[key]=chr(b) 
print(a)
