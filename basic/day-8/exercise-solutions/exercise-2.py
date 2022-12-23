n=input("Please enter any capital letter ")
for i in range(ord("A"),ord(n)+1):
    for j in range(ord("A"),ord(n)+1):
        print(chr(j),end=" ")
    print()
