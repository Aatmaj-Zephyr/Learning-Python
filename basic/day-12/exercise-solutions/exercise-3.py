a = [2, 4, 3, 7, 6, 5, 9, 10, 12]
for i in range(len(a)):
    for j in range(0, len(a) - i - 1):
        if (a[j] > a[j + 1]):
            (a[j], a[j + 1]) = (a[j + 1], a[j])  #Swapping the two
Bool = False
x = int(input("Please enter a number "))
low = 0
high = len(a) - 1
mid = 0
while low <= high:
    mid = (high + low) // 2
    if (a[mid] < x):
        low = mid + 1
    elif (a[mid] > x):
        high = mid - 1
    else:
        print(mid + 1)
        Bool = True
        break
if not Bool:
    print("not in list ")
