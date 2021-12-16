n = int(input("Enter a number"))
s = 0
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        s += i
        count += 1
print("Sum of the factors = ", s)
print("Count of the factors = ", count)
