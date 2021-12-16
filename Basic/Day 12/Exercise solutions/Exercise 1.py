a = [1, 3, 4, 6, 5, 2, 6]
Bool = False
n = int(input("Please enter the number to be searched "))
#Method-1
for i in range(len(a)):
    if (a[i] == n):
        print("Method-1 Yes, the number is in the list ")
        Bool = True
        break
#Method-2
if (n in a):
    print("Method-2 Yes, the number is in the list ")
    Bool = True

if (not Bool):
    print("Not in list")
