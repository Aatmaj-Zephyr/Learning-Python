for j in range(1,5):
 for i in range(1,j+1):
    print(chr(i+64),end="")
 for i in range(-j+1,0):
    print(chr(-i+64),end="")
 print()
