a=[1,3,5,6,8,7,10,12,14]
x=int(input("Please enter a number "))
low = 0
high = len(a) - 1
mid = 0
while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if (a[mid] < x):
            low = mid + 1
        # If x is smaller, ignore right half
        elif (a[mid] > x):
            high = mid - 1
        # means x is present at mid
        else:
            print(mid+1)
            break
        
