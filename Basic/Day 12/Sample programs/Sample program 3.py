a=[2,4,3,7,6,5,9,10,12]
 # Traverse through all array elements
for i in range(len(a)):
    # Last i elements are already in place
    for j in range(0, len(a)-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if (a[j] > a[j+1]) :
                (a[j], a[j+1]) = (a[j+1], a[j]) #Swapping the two
 
print ("Sorted array is:",a)
