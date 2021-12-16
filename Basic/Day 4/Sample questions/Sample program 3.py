a = int(input("Enter a number "))
IsPrime = 0
for i in range(2, a // 2):
    if (a % i == 0):
        print("The number is composite ")
        IsPrime = 1
        break
if (IsPrime == 0):
    print("The number is prime.")
