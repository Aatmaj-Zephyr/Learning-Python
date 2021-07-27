txt=input("Please enter a string: ")
for i in range(0,len(txt)):
 for ch in range(0, i+1):
    print(txt[ch], end=" ")
 print()
